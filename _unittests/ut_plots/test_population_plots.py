# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, add_missing_development_version


class TestPopulationPlots(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "pyrsslocal"],
                                        __file__, hide=True)

    def test_population_france2015_plots(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv()
        from matplotlib import pyplot as plt
        from actuariat_python.data import population_france_year
        from actuariat_python.plots import plot_population_pyramid

        df = population_france_year()
        self.assertEqual(df.shape[1], 5)
        self.assertEqual(list(df.columns), [
                         'naissance', 'age', 'hommes', 'femmes', 'ensemble'])
        ax = plot_population_pyramid(df["hommes"], df["femmes"])

        assert ax is not None
        # avoid matplotlib to crash later
        plt.close('all')


if __name__ == "__main__":
    unittest.main()
