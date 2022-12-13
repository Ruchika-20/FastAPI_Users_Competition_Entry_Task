from fastapi import FastAPI
from backend.routes.user_route import user
from backend.routes.competition_route import competition
from backend.routes.entry_route import entry

app=FastAPI()
app.include_router(user,tags=['user'])
app.include_router(competition,tags=['competition'])
app.include_router(entry,tags=['entry'])
