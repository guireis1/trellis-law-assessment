"""
This module contains the API routes for version 1 of the application.

It includes routers for monitoring and numbers endpoints.
"""

from fastapi import APIRouter

from .monitoring import monitoring_router
from .numbers import numbers_router

v1_router = APIRouter()
v1_router.include_router(monitoring_router, prefix="/monitoring")
v1_router.include_router(numbers_router, prefix="/numbers")
