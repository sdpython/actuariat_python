# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version


class TestElections(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pyrsslocal"], __file__)

    def test_elections_2012(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_presidentielles
        dfs = elections_presidentielles()
        fLOG(type(dfs))
        fLOG(list(dfs.keys()))
        assert len(dfs) > 0


if __name__ == "__main__":
    unittest.main()
