from backend.database.database import Base
from sqlalchemy import String, Boolean, Integer, Column, DateTime,Date,ForeignKey
from backend.models.user_model import User_model
from datetime import datetime
from backend.utils.util import Common


class Competition_model(Base, Common):
    __tablename__ = "competition"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Boolean, default = True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey(User_model.id))
