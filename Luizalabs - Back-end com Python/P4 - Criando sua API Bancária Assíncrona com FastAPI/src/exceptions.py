from http import HTTPStatus


class ErrorNotFound(Exception):
    def __init__(self, message: str = "Not found", status_code: int = HTTPStatus.NOT_FOUND) -> None:
        self.message = message
        self.status_code = status_code

class ErrorForbidden(Exception):
    def __init__(self, message: str = "Forbidden", status_code: int = HTTPStatus.FORBIDDEN) -> None:
        self.message = message
        self.status_code = status_code
