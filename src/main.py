from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from sqlalchemy.orm import clear_mappers

from config import settings
from infrastructure import engine, logger, mapper_registery
from user.orm import start_user_mapper


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    logger.warning("fastapi_app.docs_url: %s", fastapi_app.docs_url)
    mapper_registery.metadata.create_all(engine)
    start_user_mapper()
    yield
    clear_mappers()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root() -> dict:
    logger.debug("settings.app_name: %s", settings.app_name)
    return {"App name": settings.app_name, "Base directory": settings.base_directory}


if __name__ == "__main__":
    logger.info(f"Starting {settings.app_name}...")
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
