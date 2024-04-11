"""
This module provides API routes for converting numbers to English words.
"""

from fastapi import APIRouter

from .numbers import numbers_router

task_router = APIRouter()
task_router.include_router(numbers_router, prefix="/num_to_english", tags=["Numbers"])

__all__ = ["task_router"]
