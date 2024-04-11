from fastapi import APIRouter

from app.models.extras.health import Health
from core import config

health_router = APIRouter()


@health_router.get("/")
async def health() -> Health:
    """
    Endpoint to check the health status of the application.

    Returns:
        Health: An instance of the Health model containing the application version and status.
    """
    return Health(version=config.APP_VERSION, status="Healthy")
