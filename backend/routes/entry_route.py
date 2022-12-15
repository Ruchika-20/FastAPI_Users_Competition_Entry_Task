from fastapi import APIRouter, status
from backend.database.database import SessionLocal
from backend.models.entry_model import Entry_model
from backend.schemas.entry_schema import Entry_schema
from backend.models.competition_model import Competition_model


entry = APIRouter()
db = SessionLocal()


@entry.post("/entrypost", status_code=status.HTTP_201_CREATED)
def insert(entry: Entry_schema):
    """
        Inserting the entry
    Args:
        entry (Entry_schema): _description_

    Returns:
        _type_: _description_
    """
    new_entry = Entry_model(
        id=entry.id,
        title=entry.title,
        topic=entry.topic,
        state=entry.state,
        country=entry.country,
        competition_id=entry.competition_id,
    )
    db.add(new_entry)
    db.commit()

    return {"status": 200, "message": "Entry added successfully"}


@entry.get("/entry", status_code=200)
def read_all():
    """Reading all the entries

    Returns:
        _type_: _description_
    """
    entry = db.query(Entry_model).all()

    return {"data": entry, "status": 200, "message": "Entry get successfully"}


@entry.get("/entry/{entry_id}", status_code=status.HTTP_200_OK)
def read(entry_id: int):
    """Reading the entry from a given id
    Args:
        entry_id (int): _description_

    Returns:
        _type_: _description_
    """
    item = db.query(Entry_model).filter(Entry_model.id == entry_id).first()
    return {"data": item, "status": 200, "message": "entrys retrived successfully"}


@entry.put("/entryput/{entry_id}", status_code=status.HTTP_200_OK)
def update(entry_id: int, entry: Entry_schema):
    """Updating an entry

    Args:
        entry_id (int): _description_
        entry (Entry_schema): _description_

    Returns:
        _type_: _description_
    """
    entry_to_update = db.query(Entry_model).filter(Entry_model.id == entry_id).first()
    entry_to_update.id = (entry.id,)
    entry_to_update.title = (entry.title,)
    entry_to_update.topic = (entry.topic,)
    entry_to_update.state = (entry.state,)
    entry_to_update.country = (entry.country,)
    db.commit()
    return {"status": 200, "message": "Entry Details updated successfully"}


@entry.delete("/entrydelete/{entry_id}")
def delete(entry_id: int):
    """Deleting an entry

    Args:
        entry_id (int): _description_

    Returns:
        _type_: _description_
    """

    entry_to_delete = db.query(Entry_model).filter(Entry_model.id == entry_id).first()
    db.delete(entry_to_delete)
    db.commit()

    return {
        "data": entry_to_delete,
        "status": 200,
        "message": "entry deleted successfully",
    }


@entry.get("/entry/{user_id}/count")
def count_user(user_id: int):
    """A new API for counting the entries

    Args:
        user_id (_type_): _description_
        db (Session, optional): _description_. Defaults to Depends(get_db).

    Returns:
        _type_: _description_
    """
    competitions_entry = (
        db.query(Competition_model.id)
        .filter(Competition_model.user_id == user_id)
        .all()
    )

    # for loop
    competitions_entry = [competition.id for competition in competitions_entry]

    # initial result is set to zero
    result = 0
    for competition in competitions_entry:
        entry = (
            db.query(Entry_model.id)
            .filter(Entry_model.competition_id == competition)
            .count()
        )
        result += entry

    return result
