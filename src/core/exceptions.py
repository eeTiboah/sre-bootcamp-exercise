
from fastapi import status, HTTPException


class ValidationError(HTTPException):
    def __init__(self, error_msg: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error_msg
        )


class AlreadyExistsError(HTTPException):
    def __init__(self, error_msg: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=error_msg
        )


class NotFoundError(HTTPException):
    def __init__(self, error_msg: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error_msg
        )