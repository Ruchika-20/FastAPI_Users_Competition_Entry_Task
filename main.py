import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    host=os.getenv("HOST")
    port=os.getenv("PORT")
    uvicorn.run("backend.api:app", host=host, port=int(port), lifespan="on", reload=True)

    