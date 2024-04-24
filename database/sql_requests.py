from sqlmodel import SQLModel, Field
from typing import Optional


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    telegram_id: int
    telegram_teg: str
    registration_date: str
    active: bool = True
    rights: str
    user_name: str
    surname: str


class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    description: str
    creation_date: str


class Notes(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    date: str
    nate: str
    creation_date: str
    sticker: str


class Notebook(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    creation_date: str
    name: str
    text: str