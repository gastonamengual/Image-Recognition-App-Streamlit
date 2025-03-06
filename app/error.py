from dataclasses import dataclass
from app.utils import stop_execution


@dataclass
class BaseCustomException(Exception):
    message: str = ""

    def __post_init__(self):
        stop_execution(self.message)


class TokenNotObtainedError(BaseCustomException):
    pass


class DetectionNotObtained(BaseCustomException):
    pass
