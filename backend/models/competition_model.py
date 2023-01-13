from backend.database.database import Base
from sqlalchemy import String, Boolean, Column, ForeignKey
from backend.models.user_model import User_model
from backend.utils.util import Common
from sqlalchemy.dialects.postgresql import UUID


class Competition_model(Base, Common):
    """Creating a model for the Competition

    Args:
        Base (_type_): _description_
        Common (_type_): _description_
    """

    __tablename__ = "competition"
    name = Column(String)
    status = Column(Boolean, default=True)
    description = Column(String)
    user_id = Column(UUID, ForeignKey(User_model.id))
