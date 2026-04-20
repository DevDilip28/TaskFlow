from src.user import controller
from src.user.dots import UserSchema
from fastapi import APIRouter, Depends, status
from src.utils.db import get_db
from sqlalchemy.orm import Session

user_routes = APIRouter(prefix="/user")

@user_routes.post("/register", status_code=status.HTTP_201_CREATED)
def register(body: UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)
