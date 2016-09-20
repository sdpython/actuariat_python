#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest
import pandas


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
from pyquickhelper.pycode import add_missing_development_version, get_temp_folder


class TestGeocoding(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pyensae", "pymyinstall", "pyrsslocal"], __file__,
                                        hide=__name__ == "__main__")
        from src.actuariat_python.data import elections_presidentielles as skip__

    def test_geocoding(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_geocoding")
        from src.actuariat_python.data import geocode
        data = os.path.join(os.path.abspath(
            os.path.dirname(__file__)), "data", "bureau.txt")
        df = pandas.read_csv(data, sep="\t", encoding="utf-8")
        he = df.head(n=10)
        res = geocode(he)
        fLOG(res)
        out = os.path.join(temp, "geo.csv")
        res.to_csv(out, sep="\t", encoding="utf-8", index=False)
        res.to_excel(out + ".xlsx", index=False)


if __name__ == "__main__":
    unittest.main()
