from pydantic import BaseModel
from datetime import date


class User_schema(BaseModel):
    name: str
    birthdate: date
    gender: str

    class Config:
        orm_mode = True
