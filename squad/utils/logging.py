import logging
from typing import Optional


def get_logger(file_name: str, class_name: Optional[str] = None) -> logging.Logger:
    """
    Retrieves a customized logger object with a specified name based on the file name and optional class name.

    :param file_name: A string representing the name of the file where the logger is being used.
    :type file_name: str
    :param class_name: An optional string representing the name of a class. If provided, it will be used to construct
        the name of the logger. If not provided, the name of the logger will be based on the file name.
    :type class_name: Optional[str]
    :return: A logging.Logger object with a customized name.
    """
    parts = file_name.split("_")

    if parts[1].startswith("utils") and class_name is None:
        name = parts[0].rstrip(".")
    else:
        name = f"{parts[0]}{class_name or parts[1].capitalize()}"

    return logging.getLogger(name)
