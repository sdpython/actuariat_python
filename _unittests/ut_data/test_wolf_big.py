# -*- coding: utf-8 -*-
"""
@brief      test log(time=53s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


class TestWolfBig(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pyrsslocal", "pyrsslocal"],
                                        __file__, hide=True)

    def test_enumerate_wolf_synonyms_big2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import wolf_xml, enumerate_wolf_synonyms
        temp = get_temp_folder(__file__, "temp_enumerate_wolf_xml_row_big2")
        wolf_xml(temp_folder=temp)
        data = os.path.join(temp, "wolf-1.0b4.xml")
        rows = enumerate_wolf_synonyms(data, fLOG=fLOG, encoding="utf-8")
        nb = 0
        for _ in rows:
            nb += 1
        self.assertTrue(nb > 0)


if __name__ == "__main__":
    unittest.main()
