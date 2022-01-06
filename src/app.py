import logging
from fastapi import FastAPI

from src.router.index_router import router as index_router
from src.router.teacher_router import router as food_router


def create_app() -> FastAPI:
    app_ = FastAPI()
    return app_


logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
app = create_app()
app.include_router(index_router, prefix='/api')
app.include_router(food_router, prefix='/api/teacher')


@app.on_event('startup')
async def on_start_app():
    logger.info("start server")


@app.on_event('shutdown')
async def on_shutdown_app():
    logger.info("shutdown server")
