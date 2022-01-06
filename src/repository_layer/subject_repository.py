from src.repository_layer.base import CRUDBase
import src.domain as domain
import src.models as models


class SubjectRepository(CRUDBase[models.Subject, domain.Subject, domain.Subject]):
    pass


subject_repository = SubjectRepository(models.Subject)
