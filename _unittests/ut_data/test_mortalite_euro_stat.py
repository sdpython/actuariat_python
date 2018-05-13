# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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


from src.actuariat_python.data import table_mortalite_euro_stat


class TestMortaliteTable_EuroStat(unittest.TestCase):

    def test_population_france2015(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_table_mortalite_euro_stat")
        outfile = os.path.join(temp, "mortalite_table.txt")
        table_mortalite_euro_stat(
            whereTo=temp, final_name=outfile, fLOG=fLOG, stop_at=100)
        assert os.path.exists(outfile)


if __name__ == "__main__":
    unittest.main()
