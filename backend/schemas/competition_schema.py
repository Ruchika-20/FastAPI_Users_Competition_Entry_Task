from pydantic import BaseModel

class Competition_schema(BaseModel):
    id:int
    name : str
    description: str
    user_id : int

    class Config:
        orm_mode=True
