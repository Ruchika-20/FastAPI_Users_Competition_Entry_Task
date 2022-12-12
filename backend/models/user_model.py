from backend.database.database import Base
from sqlalchemy import String, Boolean, Integer, Column, DateTime,Date
from datetime import datetime
from backend.utils.util import Common

class User_model(Base,Common):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date)
    gender=Column(String,nullable=False)
    is_active=Column(Boolean,default=True)  