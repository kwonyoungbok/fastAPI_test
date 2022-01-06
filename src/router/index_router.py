import logging
from fastapi import APIRouter, Depends, HTTPException

logger = logging.getLogger(__name__)
router = APIRouter(tags=["index"])


@router.get(
    "/",
    responses={200: {"description": "ok"}},
)
async def index() -> dict:
    return {"system": True}
