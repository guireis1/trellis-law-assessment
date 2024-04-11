from pydantic import UUID4, BaseModel, Field


class NumberResponse(BaseModel):
    """
    Represents a response containing a number in English and its status.

    Attributes:
        num_in_english (str): The number in English plain text.
        status (str): The completed status.

    """
    num_in_english: str = Field(
        ...,
        description="Number in English Plain Text",
        example="two hundred thirty four",
    )
    status: str = Field(alias="status", description="Completed status")

    class Config:
        orm_mode = True
