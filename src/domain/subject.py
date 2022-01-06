from pydantic import BaseModel, HttpUrl

from typing import Sequence


class Subject(BaseModel):
    name: str


