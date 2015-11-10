#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import re

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper

try:
    import pyensae
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyensae",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyensae

try:
    import pymyinstall
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pymyinstall

try:
    import pyrsslocal
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyrsslocal",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyrsslocal

from pyquickhelper import fLOG, get_temp_folder
from src.actuariat_python.data import wolf_xml, enumerate_wolf_xml_row, enumerate_wolf_synonyms


class TestWolf(unittest.TestCase):

    def test_wolf(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_wolf")
        outfile = wolf_xml(fLOG=fLOG, temp_folder=temp)
        for o in outfile:
            fLOG(o)
            assert os.path.exists(o)
        assert os.stat(outfile[1]).st_size < 2000

    def test_enumerate_wolf_xml_row(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_enumerate_wolf_xml_row")
        data = os.path.join(temp, "..", "data", "sample.wolf.xml")
        rows = enumerate_wolf_xml_row(data, fLOG=fLOG, encoding=None)
        for row in rows:
            fLOG(type(row))

    def test_enumerate_wolf_synonyms(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_enumerate_wolf_xml_row")
        data = os.path.join(temp, "..", "data", "sample.wolf.xml")
        rows = enumerate_wolf_synonyms(data, fLOG=fLOG, encoding=None)
        for row in rows:
            fLOG(row)

    def test_enumerate_wolf_synonyms_big(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_enumerate_wolf_xml_row")
        data = os.path.join(temp, "..", "data", "wolf-1.0b4.xml")
        if os.path.exists(data):
            rows = enumerate_wolf_synonyms(data, fLOG=fLOG)
            for i, row in enumerate(rows):
                fLOG(row)
                if i > 300:
                    break


if __name__ == "__main__":
    unittest.main()
