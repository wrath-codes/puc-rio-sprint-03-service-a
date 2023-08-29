from pydantic import BaseModel


class ParentBase(BaseModel):
    id: int


class Parent(ParentBase):
    id: int

    class Config:
        orm_mode = True
