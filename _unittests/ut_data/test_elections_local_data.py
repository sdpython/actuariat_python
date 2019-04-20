# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version, get_temp_folder


class TestElectionsLocalData(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pyensae", "pymyinstall", "pyrsslocal"], __file__,
                                        hide=__name__ == "__main__")

    def test_villes_geo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_villes_geo")
        from actuariat_python.data import villes_geo
        res = villes_geo(folder=temp)
        fLOG(res)


if __name__ == "__main__":
    unittest.main()
