from pydantic import BaseModel, Field


class Health(BaseModel):
    """
    Represents the health status of the application.

    Attributes:
        version (str): The version of the application.
        status (str): The status of the application.
    """

    version: str = Field(..., example="1.0.0")
    status: str = Field(..., example="OK")
