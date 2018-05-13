# -*- coding: utf-8 -*-
"""
@brief      test log(time=1060s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version


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


class TestLONGPopulationPopulation(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pyrsslocal", "mlstatpy", "jyquickhelper"], __file__)

    def test_long_population_france_year(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.actuariat_python.data import population_france_year
        df = population_france_year()
        self.assertEqual(df.shape, (101, 5))


if __name__ == "__main__":
    unittest.main()
