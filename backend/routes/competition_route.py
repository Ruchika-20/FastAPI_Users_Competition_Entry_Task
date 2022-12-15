from fastapi import APIRouter, status
from backend.database.database import SessionLocal
from backend.models.competition_model import Competition_model
from backend.schemas.competition_schema import Competition_schema

competition = APIRouter()

db = SessionLocal()


@competition.post("/competitionpost", status_code=status.HTTP_201_CREATED)
def insert(competition: Competition_schema):
    """Adding a competition

    Args:
        competition (Competition_schema): _description_

    Returns:
        _type_: _description_
    """
    new_competition = Competition_model(
        name=competition.name,
        description=competition.description,
        user_id=competition.user_id,
    )
    db.add(new_competition)
    db.commit()

    return {"status": 200, "message": "competition added successfully"}


@competition.get("/competition", status_code=200)
def read_all():
    """Reading the data of competition table

    Returns:
        _type_: _description_
    """
    competition = db.query(Competition_model).all()

    return {
        "data": competition,
        "status": 200,
        "message": "competition get successfully",
    }


@competition.get("/competition/{competition_id}", status_code=status.HTTP_200_OK)
def read(competition_id: int):
    """Reading the data of competition table by id

    Args:
        competition_id (int): _description_

    Returns:
        _type_: _description_
    """
    item = (
        db.query(Competition_model)
        .filter(Competition_model.id == competition_id)
        .first()
    )

    return {
        "data": item,
        "status": 200,
        "message": "competitions retrived successfully",
    }


@competition.put("/competitionput/{competition_id}", status_code=status.HTTP_200_OK)
def update(competition_id: int, competition: Competition_schema):
    """updating the values in competition table

    Args:
        competition_id (int): _description_
        competition (Competition_schema): _description_

    Returns:
        _type_: _description_
    """
    competition_to_update = (
        db.query(Competition_model)
        .filter(Competition_model.id == competition_id)
        .first()
    )
    competition_to_update.name = (competition.name,)
    competition_to_update.description = (competition.description,)
    competition_to_update.user_id = competition.user_id
    db.commit()

    return {"status": 200, "message": "competition Details updated successfully"}


@competition.delete("/competitiondelete/{competition_id}")
def delete(competition_id: int):
    """Deleting the entry from the competition table

    Args:
        competition_id (int): _description_

    Returns:
        _type_: _description_
    """
    competition_to_delete = (
        db.query(Competition_model)
        .filter(Competition_model.id == competition_id)
        .first()
    )
    db.delete(competition_to_delete)
    db.commit()

    return {
        "data": competition_to_delete,
        "status": 200,
        "message": "competition deleted successfully",
    }
