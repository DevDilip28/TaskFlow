from src.user.dtos import UserSchema, LoginSchema
from src.user.models import UserModel
from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Request
from pwdlib import PasswordHash
from src.utils.setting import settings
import jwt
from datetime import datetime, timedelta
from jwt.exceptions import InvalidTokenError

password_hash = PasswordHash.recommended()

def get_hash_password(password):
    return password_hash.hash(password)

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def register(body: UserSchema, db: Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()

    if is_user:
        raise HTTPException(status_code=400, detail="Username already exist...")
    
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()

    if is_user:
        raise HTTPException(status_code=400, detail="Email already exist...")

    hash_password = get_hash_password(body.password)

    new_user = UserModel(
        name = body.name,
        username = body.username,
        hash_password = hash_password,
        email = body.email 
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user

def login_user(body: LoginSchema, db: Session):
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()

    if not is_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username...")
    
    if not verify_password(body.password, is_user.hash_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password...")
    
    exp_time = datetime.now() + timedelta(minutes=settings.EXPIRE_TIME)

    token = jwt.encode({"_id": is_user.id, "exp": exp_time.timestamp()}, settings.SECRET_KEY, settings.ALGORITHM)

    return {"token": token}

def is_authenticated(request: Request, db: Session):
    try:
        token = request.headers.get("Authorization")

        if not token:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token not found...")

        token = token.split(" ")[-1]

        data = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)

        user_id = data.get("_id")
        
        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found...")
        
        return user
    
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token...")
