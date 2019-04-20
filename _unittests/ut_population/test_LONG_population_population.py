# -*- coding: utf-8 -*-
"""
@brief      test log(time=1060s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version


class TestLONGPopulationPopulation(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pyrsslocal", "mlstatpy", "jyquickhelper"], __file__)

    def test_long_population_france_year(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from actuariat_python.data import population_france_year
        df = population_france_year()
        self.assertEqual(df.shape, (101, 5))


if __name__ == "__main__":
    unittest.main()
