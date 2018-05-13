# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
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


class TestPopulationMortalite(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "pyrsslocal"],
                                        __file__, hide=True)

    def test_mortalite_france(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.actuariat_python.data import table_mortalite_france_00_02
        df = table_mortalite_france_00_02()
        fLOG(df.shape)
        fLOG(df.columns)
        self.assertTrue(len(df) > 50)
        self.assertEqual(df.shape[1], 3)


if __name__ == "__main__":
    unittest.main()
