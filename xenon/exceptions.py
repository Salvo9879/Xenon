
# Import internal modules
from xenon.helpers import get_class_name

# Import external modules
import logging
import werkzeug.exceptions as http_exceptions

class BaseException(Exception):
    def __init__(self, message: str, logger: logging.Logger) -> None:
        """ `message: str ->` A message which will be returned to the exception handler.
        `logger: logging.Logger ->` a Logger object which sorts out where the information goes. """

        super().__init__(message)

        exception = get_class_name(self)
        logger.error(f"{exception}: {message}")