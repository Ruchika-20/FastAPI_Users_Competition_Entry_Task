from backend.database.database import Base
from sqlalchemy import String, Column, ForeignKey
from backend.models.competition_model import Competition_model
from backend.utils.util import Common
from sqlalchemy.dialects.postgresql import UUID


class Entry_model(Base, Common):
    """Creating the model for entry

    Args:
        Base (_type_): _description_
        Common (_type_): _description_
    """

    __tablename__ = "entry"
    title = Column(String, nullable=False)
    topic = Column(String)
    state = Column(String)
    country = Column(String)
    competition_id = Column(UUID, ForeignKey(Competition_model.id))
