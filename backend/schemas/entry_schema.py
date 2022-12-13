from pydantic import BaseModel

class Entry_schema(BaseModel):
    id : int
    title : str
    topic : str
    state : str
    country : str
    competition_id : int

    class Config:
        orm_mode=True
