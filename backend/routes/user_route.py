from fastapi import APIRouter,status, HTTPException
from backend.database.database import SessionLocal
from backend.models.user_model import User_model
from backend.schemas.user_schema import User_schema


user= APIRouter()
db = SessionLocal()


@user.post("/userpost",status_code=status.HTTP_201_CREATED)
def insert(user:User_schema):
    new_user = User_model(
        id=user.id,
        name=user.name,
        birthdate=user.birthdate,
        gender=user.gender
    )
    db.add(new_user)
    db.commit()
    return {"status": 200, "message": "User added successfully"}


@user.get("/user",status_code=200)
def read_all():
    user = db.query(User_model).all()
    return {"data": user, "status": 200, "message": "User get successfully"}
    
@user.get('/user/{user_id}', status_code=status.HTTP_200_OK)
def read(user_id: int):
    item = db.query(User_model).filter(User_model.id == user_id).first()
    # return item
    return {"data": item, "status": 200, "message": "Users retrived successfully"}

    
@user.put("/userput/{user_id}",status_code=status.HTTP_200_OK)
def update(user_id:int,user:User_schema):

    user_to_update = db.query(User_model).filter(User_model.id == user_id).first()
    user_to_update.id = user.id
    user_to_update.name = user.name,
    user_to_update.birthdate = user.birthdate,
    user_to_update.gender = user.gender,
    db.commit()
    return {"status": 200, "message": "User Details updated successfully"}


@user.delete("/userdelete/{user_id}")
def delete(user_id:int):
    user_to_delete = db.query(User_model).filter(User_model.id == user_id).first()
    db.delete(user_to_delete)
    db.commit()
    return user_to_delete
    




    


   

