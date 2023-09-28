from pydantic import BaseModel


class ErrorResponseSchema(BaseModel):
    mesage: str