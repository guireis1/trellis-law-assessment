"""
This module contains the monitoring API router.

It includes the health router and defines the monitoring_router, which is used to group all the monitoring related routes.
"""

from fastapi import APIRouter

from .health import health_router

monitoring_router = APIRouter()
monitoring_router.include_router(health_router, prefix="/health", tags=["Health"])

__all__ = ["monitoring_router"]
