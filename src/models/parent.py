from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from src.config.database import Base


class Parent(Base):
    """Parent model"""

    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, autoincrement=True)

    children = relationship("Child", back_populates="parent")
