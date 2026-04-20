from src.user.dtos import UserSchema
from src.user.models import UserModel
from sqlalchemy.orm import Session
from fastapi import HTTPException
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def get_hash_password(password):
    return password_hash.hash(password)

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

