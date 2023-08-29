from datetime import date

from pydantic import BaseModel


class ChildBase(BaseModel):
    name: str
    birth_date: date
    parent_id: int


class ChildCreate(ChildBase):
    parent_id: int


class ChildUpdate(ChildBase):
    pass


class Child(ChildBase):
    id: int
    parent_id: int

    class Config:
        orm_mode = True
