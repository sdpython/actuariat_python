#-*- coding: utf-8 -*-
"""
@file
@brief Main file
"""

import sys
if sys.version_info[0] < 3:
    raise ImportError("pyensae only works with Python 3")

__version__ = "0.1"
__author__ = "Vincent Bernardi, Xavier Dupré"
__github__ = "https://github.com/sdpython/actuariat_python"
__url__ = "http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#actuariat_python"
__license__ = "MIT License"


def _setup_hook():
    """
    does nothing
    """
    pass


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True
