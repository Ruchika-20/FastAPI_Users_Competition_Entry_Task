from pydantic import BaseModel
from datetime import date

class User_schema(BaseModel):
    id : int
    name : str
    birthdate : date               
    gender : str 
    # created_at : str
    # updated_at : str
    # is_active : bool
    # is_delete : bool

    class Config:
        orm_mode=True
    