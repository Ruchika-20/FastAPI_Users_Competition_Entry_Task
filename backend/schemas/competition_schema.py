from pydantic import BaseModel


class Competition_schema(BaseModel):

    name: str
    description: str
    user_id: str

    class Config:
        orm_mode = True
