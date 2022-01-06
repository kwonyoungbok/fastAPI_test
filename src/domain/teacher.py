from pydantic import BaseModel, HttpUrl
from src.models.teacher import Teacher as TeacherModel


class Teacher(BaseModel):
    name: str

    @staticmethod
    def create_by_model(m: TeacherModel):
        return Teacher(**{
            "name": m.name
        })
