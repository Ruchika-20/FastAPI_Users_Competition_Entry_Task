from fastapi import APIRouter,status, HTTPException
from backend.database.database import SessionLocal
from backend.models.entry_model import Entry_model
from backend.schemas.entry_schema import Entry_schema

entry= APIRouter()
db = SessionLocal()

@entry.post("/entrypost",status_code=status.HTTP_201_CREATED)
def insert(entry:Entry_schema):
    new_entry = Entry_model(
        id=entry.id,
        title=entry.title,
        topic=entry.topic,
        state=entry.state,
        country=entry.country,
        competition_id=entry.competition_id)
    db.add(new_entry)
    db.commit()
    return {"status": 200, "message": "Entry added successfully"}

@entry.get("/entry",status_code=200)
def read_all():
    entry = db.query(Entry_model).all()
    return {"data": entry, "status": 200, "message": "Entry get successfully"}
    
@entry.get('/entry/{entry_id}', status_code=status.HTTP_200_OK)
def read(entry_id: int):
    item = db.query(Entry_model).filter(Entry_model.id == entry_id).first()
    return {"data": item, "status": 200, "message": "entrys retrived successfully"}
 
@entry.put("/entryput/{entry_id}",status_code=status.HTTP_200_OK)
def update(entry_id:int,entry:Entry_schema):
    entry_to_update = db.query(Entry_model).filter(Entry_model.id == entry_id).first()
    entry_to_update.id = entry.id,
    entry_to_update.title = entry.title,
    entry_to_update.topic = entry.topic,
    entry_to_update.state = entry.state,
    entry_to_update.country = entry.country,
    db.commit()
    return {"status": 200, "message": "Entry Details updated successfully"}

@entry.delete("/entrydelete/{entry_id}")
def delete(entry_id:int):
    entry_to_delete = db.query(Entry_model).filter(Entry_model.id == entry_id).first()
    db.delete(entry_to_delete)
    db.commit()
    return {"data": entry_to_delete, "status": 200, "message": "entry deleted successfully"}
    
    
    