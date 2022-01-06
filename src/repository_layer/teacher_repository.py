from src.repository_layer.base import CRUDBase
import src.domain as domain
import src.models as models


class TeacherRepository(CRUDBase[models.Teacher, domain.Teacher, domain.Teacher]):
    pass


teacher_repository = TeacherRepository(models.Teacher)
