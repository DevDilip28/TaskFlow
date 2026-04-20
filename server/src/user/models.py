from sqlalchemy import Column, Integer, String, DateTime
from src.utils.db import Base

class UserModel(Base):
    __tablename__ = "user_info"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, nullable=False, unique=True)
    email = Column(String)
    hash_password = Column(String, nullable=False)
    created_at = Column(DateTime)
