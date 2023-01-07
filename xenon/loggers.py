
# Import external modules
import logging

LOGGING_FILE_PATH = 'instance/logs/'

# Logger class
def new_logger(name: str, formatter: str = '[%(levelname)s - %(levelno)s] | %(asctime)s | Line: %(lineno)d | Via: "%(name)s" | Msg: "%(message)s"', level: int = logging.INFO) -> logging.Logger:
    """ Creates, configures & formats a new logger which can be used across the server. """

    handler = logging.FileHandler(f"{LOGGING_FILE_PATH}{name}.log")
    handler.setFormatter(logging.Formatter(formatter))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Create logger
govee_logger = new_logger('govee')
xenon_requests = new_logger('xenon_requests')