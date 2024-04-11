from typing import Optional

from fastapi import APIRouter, Depends, Query

from core.security import auth
from app.controllers import NumberController
from app.models.requests.numbers import NumberRequest
from app.models.responses.numbers import NumberResponse

numbers_router = APIRouter(tags=['Numbers'])


@numbers_router.post("/num_to_english", response_model=NumberResponse, status_code=201)
async def convert_number_to_english(
    number_request: NumberRequest,
    number_controller: NumberController = Depends(NumberController),
    _: bool = Depends(auth.validate_request),
) -> NumberResponse:
    """
    Convert a number to its English representation.

    Args:
        number_request (NumberRequest): The request object containing the number to convert.
        number_controller (NumberController): The controller for number conversion.

    Returns:
        NumberResponse: The response object containing the converted number in English.
    """
    return await number_controller.convert_to_english(number_request.number)


@numbers_router.get("/num_to_english", response_model=NumberResponse, status_code=200)
async def convert_number_to_english_get(
    number: Optional[str] = Query(None, regex=r"^-?\d{1,33}$"),
    number_controller: NumberController = Depends(NumberController),
    _: bool = Depends(auth.validate_request),
) -> NumberResponse:
    """
    Convert a number to its English representation.

    Args:
        number (str, optional): The number to convert. Defaults to None.
        number_controller (NumberController): The controller for number conversion.

    Returns:
        NumberResponse: The response object containing the converted number in English.
    """
    return await number_controller.convert_to_english(number)
