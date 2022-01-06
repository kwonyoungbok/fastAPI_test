from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, HttpUrl

from src.db.base import Base


class Subject(Base):
    id = Column(Integer, primary_key=True, index=True)  # 2
    name = Column(String(64), nullable=False)
    # teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=True)





