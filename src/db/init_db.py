import logging
from sqlalchemy.orm.session import Session
import src.repository_layer as repositories
import src.models as models
import src.domain as domain

from src import repository_layer, domain
from src.db.base import Base as DBBase

logger = logging.getLogger(__name__)

FIRST_SUPERUSER = "권영복"


def init_db(db: Session) -> None:
    teacher = domain.Teacher(**{
        "name": "권영복"
    })
    subject1 = domain.Subject(**{
        "name": "파이썬"
    })
    subject2 = domain.Subject(**{
        "name": "자바"
    })

    teacher_model = repositories.teacher_repository.create(db, obj_in=teacher)
    subject1_model = repositories.subject_repository.create(db, obj_in=subject1)
    subject2_model = repositories.subject_repository.create(db, obj_in=subject2)
    print(subject1_model.id)
    teacher_subject1 = domain.TeacherSubject(**{
        "teacher_id": teacher_model.id,
        "subject_id": subject1_model.id,
        "price": 10
    })
    teacher_subject2 = domain.TeacherSubject(**{
        "teacher_id": teacher_model.id,
        "subject_id": subject2_model.id,
        "price": 10
    })
    teacher_subject1_model = repositories.teacher_subject_repository.create(db, obj_in=teacher_subject1)
    teacher_subject2_model = repositories.teacher_subject_repository.create(db, obj_in=teacher_subject2)


