from sqlalchemy import Column, Date, Integer, String, Table

from infrastructure import mapper_registery

user_table = Table(
    "user",
    mapper_registery.metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("mobile", String, nullable=False),
    Column("email", String, nullable=True),
    Column("first_name", String, nullable=True),
    Column("last_name", String, nullable=True),
    Column("hashed_password", String, nullable=False),
    Column("registration_date", Date, nullable=False),
)
