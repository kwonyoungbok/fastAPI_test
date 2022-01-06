from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.base import Base


class TeacherSubject(Base):
    __tablename__ = "teacher_subject"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer, default=0)
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship("Teacher")
    subject_id = Column(Integer, ForeignKey('subject.id'))
    subject = relationship("Subject")
