import logging

import uvicorn
from fastapi import FastAPI

from config import settings
from infrastructure.database import engine, mapper_registery

app = FastAPI()


mapper_registery.metadata.create_all(bind=engine)


@app.get("/")
async def root() -> dict:
    return {"App name": settings.app_name, "Base directory": settings.base_directory}


if __name__ == "__main__":
    logging.debug("App Starting ...")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
