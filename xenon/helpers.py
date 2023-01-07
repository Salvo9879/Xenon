
# Import external modules
import datetime

def get_class_name(s: any) -> str:
    """ Gets the class name of a object. """
    return type(s).__name__

def convert_iso_to_dt(iso_dt: str) -> datetime.datetime:
    """ Converts a iso string to a `datetime.datetime`. """
    return datetime.datetime.now().fromisoformat(iso_dt)