from pydantic import BaseModel, constr


class NumberRequest(BaseModel):
    """
    Represents a request for a number.

    Attributes:
        number (str): The number to be requested. Must be a string representation of an integer
                      with a maximum of 33 digits, allowing for a negative sign at the beginning.
    """
    number: constr(regex=r"^-?\d{1,33}$")
