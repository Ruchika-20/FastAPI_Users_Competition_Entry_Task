from backend.database.database import Base
from sqlalchemy import String, Boolean, Integer, Column, DateTime,Date,ForeignKey
from backend.models.competition_model import Competition_model
from datetime import datetime
from backend.utils.util import Common

#Creating the model for entry
class Entry_model(Base,Common):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    topic = Column(String)
    state= Column(String)
    country= Column(String)
    competition_id=Column(Integer,ForeignKey(Competition_model.id))
