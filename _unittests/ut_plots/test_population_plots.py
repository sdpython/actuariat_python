#-*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
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
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from src.actuariat_python.data import population_france_2015
from src.actuariat_python.plots import plot_population_pyramid


class TestPopulationPlots(unittest.TestCase):

    def test_population_france2015_plots(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv()
        from matplotlib import pyplot as plt

        df = population_france_2015()
        ax = plot_population_pyramid(df["hommes"], df["femmes"])
        assert ax is not None
        # avoid matplotlib to crash later
        plt.close('all')


if __name__ == "__main__":
    unittest.main()
