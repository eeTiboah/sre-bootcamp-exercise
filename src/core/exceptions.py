
from fastapi import status


class ValidationError(Exception):
    def __init__(self, error_msg: str):
        super().__init__(error_msg)
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.error_msg = error_msg


class AlreadyExistsError(Exception):
    def __init__(self, error_msg: str):
        super().__init__(error_msg)
        self.status_code = status.HTTP_409_CONFLICT
        self.error_msg = error_msg


class NotFoundError(Exception):
    def __init__(self, error_msg: str):
        super().__init__(error_msg)
        self.status_code = status.HTTP_404_NOT_FOUND
        self.error_msg = error_msg