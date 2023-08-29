from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.config.database import Base


class Child(Base):
    """Child model"""

    __tablename__ = "children"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    birth_date = Column(Date, nullable=False)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)

    parent = relationship("Parent", back_populates="children")
