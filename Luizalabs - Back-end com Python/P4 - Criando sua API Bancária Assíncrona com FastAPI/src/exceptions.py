from http import HTTPStatus


class Error_401_UNAUTHORIZED(Exception):
    def __init__(self, message: str = "Unauthorized", status_code: int = HTTPStatus.UNAUTHORIZED) -> None:
        self.message = message
        self.status_code = status_code

class Error_403_FORBIDDEN(Exception):
    def __init__(self, message: str = "Forbidden", status_code: int = HTTPStatus.FORBIDDEN) -> None:
        self.message = message
        self.status_code = status_code
class Error_404_NOT_FOUND(Exception):
    def __init__(self, message: str = "Not found", status_code: int = HTTPStatus.NOT_FOUND) -> None:
        self.message = message
        self.status_code = status_code

class Error_406_NOT_ACCEPTABLE(Exception):
    def __init__(self, message: str = "Not Acceptable", status_code: int = HTTPStatus.NOT_ACCEPTABLE) -> None:
        self.message = message
        self.status_code = status_code
