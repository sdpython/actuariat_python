#-*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest


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
    import pyquickhelper as skip_
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
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.actuariat_python.data import fecondite_france


class TestPopulationFecondite(unittest.TestCase):

    def test_population_fecondite(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        df = fecondite_france()
        fLOG(df.shape)
        assert len(df) > 35
        assert df.shape[1] == 3
        fLOG(df.columns)
        fLOG(df.dtypes)
        fLOG(df.head())
        fLOG(df.tail())


if __name__ == "__main__":
    unittest.main()
