from sqlalchemy import Column, Integer, String, ForeignKey

from src.db.base import Base


class Teacher(Base):
    id = Column(Integer, primary_key=True, index=True)  # 2
    name = Column(String(32), nullable=False)
