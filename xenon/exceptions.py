
# Import internal modules
from helpers import get_class_name

# Import external modules
import logging

class BaseException(Exception):
    def __init__(self, message: str, logger: logging.Logger) -> None:
        super().__init__(message)

        exception = get_class_name(self)
        logger.error(f"{exception}: {message}")

class Apis():
    class Govee():
        class FailedToCreateDevice(BaseException):
            """ Raised when the `xenon.databases.Govee()` database manager attempts to add & commit a row to the database which results the action to fail. This is a development error. """