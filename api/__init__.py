"""
This module serves as the entry point for the API endpoints.

It defines the main router object that includes the version 1 router.
"""

from fastapi import APIRouter

from .v1 import v1_router

router = APIRouter()
router.include_router(v1_router, prefix="/v1")


__all__ = ["router"]
