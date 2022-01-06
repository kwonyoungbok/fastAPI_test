from pydantic import BaseModel, HttpUrl
from typing import Sequence

import src.domain as domain


class TeacherSubject(BaseModel):
    subject_id: int
    teacher_id: int
    price: int

