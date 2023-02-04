# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


class TestWolfBackup(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pyrsslocal", "pyrsslocal"],
                                        __file__, hide=True)

    def test_wolf_backup(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_wolf_backup")
        from pyensae.datasource import download_data
        res = download_data("wolf-1.0b4.xml.zip", whereTo=temp, fLOG=fLOG)
        self.assertEqual(len(res), 1)
        outfile = [os.path.join(temp, _) for _ in os.listdir(temp)]
        self.assertTrue(len(outfile) != 0)
        if os.stat(outfile[0]).st_size < 1000000:
            raise AssertionError("small size")


if __name__ == "__main__":
    unittest.main()
