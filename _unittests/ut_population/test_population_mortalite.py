#-*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
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

from pyquickhelper import fLOG, get_temp_folder
from src.actuariat_python.data import population_france_2015


class TestPopulationMortalite(unittest.TestCase):

    def test_population_france2015(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        df = population_france_2015()
        assert df.shape == (101, 5)

        # outfile = os.path.join(temp, "out_france.csv")
        #temp = get_temp_folder(__file__, "temp_population_france2015")
        #df.to_csv(outfile, sep="\t", index=False, encoding="utf8")


if __name__ == "__main__":
    unittest.main()
