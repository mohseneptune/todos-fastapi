from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry, sessionmaker

from config import settings

# database_url = f"{settings.database_dialect}:// \
#     {settings.database_user}:{settings.database_password}@ \
#     {settings.database_host}:{settings.database_port}/{settings.database_name}"

database_url = f"sqlite:///{settings.base_directory}/todos.db"


engine = create_engine(database_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

mapper_registery = registry()
