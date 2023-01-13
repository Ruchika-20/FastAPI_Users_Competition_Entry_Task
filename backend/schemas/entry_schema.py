from pydantic import BaseModel


class Entry_schema(BaseModel):
    title: str
    topic: str
    state: str
    country: str
    competition_id: str

    class Config:
        orm_mode = True
