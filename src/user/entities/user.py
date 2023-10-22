from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class User:
    id: int
    username: str
    mobile: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    hashed_password: str
    registration_date: date
