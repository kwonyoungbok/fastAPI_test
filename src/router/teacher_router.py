import logging
from fastapi import APIRouter, Depends, HTTPException
from typing import List
import src.domain as domain
import src.models as models
import src.repository_layer as repositories
import src.deps as deps

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Teacher"])


@router.get(
    "/{teacher_id}",
    response_model=domain.Teacher
)
async def teacher_find_by_id(*, teacher_id: int, db=Depends(deps.get_db)) -> dict:
    teacher_model = repositories.teacher_repository.get(db, id=teacher_id)
    if not teacher_model:
        raise HTTPException(
            status_code=404, detail=f"Not Found Teacher id:{teacher_id}"
        )
    return domain.Teacher.create_by_model(teacher_model)


@router.get(
    "/teacher_subject/{teacher_id}",
    #response_model=domain.Teacher
)
async def teacher_subject_find_by_id(*, teacher_id: int, db=Depends(deps.get_db)) -> dict:
    result = repositories.teacher_subject_repository.get_all_by_teacher_id(db, teacher_id=teacher_id)
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Not Found Teacher_subject id:{teacher_id}"
        )
    subject_list = [r.subject.name for r in result]
    return {"subjects": subject_list}

