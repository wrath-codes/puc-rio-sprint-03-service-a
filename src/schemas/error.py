from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """Defines the error schema"""

    message: str
