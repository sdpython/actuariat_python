"""
@file
@brief Exceptions raised by this module when getting data
"""


class DataNotAvailableError(Exception):
    """
    raised data is not available
    """
    pass


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
