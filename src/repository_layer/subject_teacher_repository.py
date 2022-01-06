from typing import List
from sqlalchemy.orm import Session

import src.domain as domain
import src.models as models
from src.repository_layer.base import CRUDBase


class TeacherSubjectRepository(CRUDBase[models.TeacherSubject, domain.TeacherSubject, domain.TeacherSubject]):
    def get_all_by_teacher_id(self, db: Session, teacher_id: int) -> List[models.TeacherSubject]:
        return db.query(self.model).filter(
            self.model.teacher_id == teacher_id
        ).all()


teacher_subject_repository = TeacherSubjectRepository(models.TeacherSubject)
