"""
@file
@brief Exception raised while getting data
"""


class DataFormatException(Exception):

    """
    raise when the format is unexpected
    """
    pass


class LinkNotFoundError(Exception):

    """
    raise when a file is not found on a webpage
    """
    pass
