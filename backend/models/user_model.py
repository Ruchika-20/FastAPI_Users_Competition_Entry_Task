from backend.database.database import Base
from sqlalchemy import String, Boolean, Integer, Column, Date
from backend.utils.util import Common

#
class User_model(Base, Common):
    """Creating a model for the user

    Args:
        Base (_type_): _description_
        Common (_type_): _description_
    """

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthdate = Column(Date)
    gender = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
