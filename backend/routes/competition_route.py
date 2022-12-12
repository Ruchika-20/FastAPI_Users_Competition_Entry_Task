from fastapi import APIRouter,status, HTTPException
from backend.database.database import SessionLocal
from backend.models.competition_model import Competition_model
from backend.schemas.competition_schema import Competition_schema

competition= APIRouter()
db = SessionLocal()

#Adding a competition
@competition.post("/competitionpost",status_code=status.HTTP_201_CREATED)
def insert(competition:Competition_schema):
    new_competition = Competition_model(
        name=competition.name,
        # status=competition.status,
        description=competition.description,
        user_id=competition.user_id
    )
    db.add(new_competition)
    db.commit()
    return {"status": 200, "message": "competition added successfully"}

#Reading the data of competition table
@competition.get("/competition",status_code=200)
def read_all():
    competition = db.query(Competition_model).all()
    return {"data": competition, "status": 200, "message": "competition get successfully"}
    

@competition.get('/competition/{competition_id}', status_code=status.HTTP_200_OK)
def read(competition_id: int):
    item = db.query(Competition_model).filter(Competition_model.id == competition_id).first()
    return {"data": item, "status": 200, "message": "competitions retrived successfully"}


#updating the values in competition table   
@competition.put("/competitionput/{competition_id}",status_code=status.HTTP_200_OK)
def update(competition_id:int,competition:Competition_schema):
    competition_to_update = db.query(Competition_model).filter(Competition_model.id == competition_id).first()
    competition_to_update.name = competition.name,
    competition_to_update.description = competition.description,
    competition_to_update.user_id=competition.user_id
    db.commit()
    return {"status": 200, "message": "competition Details updated successfully"}

#Deleting the entry from the competition table
@competition.delete("/competitiondelete/{competition_id}")
def delete(competition_id:int):
    competition_to_delete = db.query(Competition_model).filter(Competition_model.id == competition_id).first()
    db.delete(competition_to_delete)
    db.commit()
    return {"data": competition_to_delete, "status": 200, "message": "competition deleted successfully"}
    
    
    