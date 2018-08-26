# -*- coding: utf-8 -*-
"""
@brief      test log(time=16s)
"""

import sys
import os
import unittest
import warnings
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version, get_temp_folder, is_travis_or_appveyor, ExtTestCase


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


class TestGeocoding(ExtTestCase):

    def setUp(self):
        add_missing_development_version(["pyensae", "pymyinstall", "pyrsslocal"], __file__,
                                        hide=__name__ == "__main__")

    @unittest.skipIf(is_travis_or_appveyor() is not None, "no keys")
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
        he = df.head(n=5)
        every = os.path.join(temp, "every.csv")

        # we retrieve an encrypted key
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            import keyring

        bing_key = keyring.get_password("bing", "actuariat_python,key")
        self.assertNotEmpty(bing_key)
        fLOG(bing_key)
        coders = ["Nominatim"]
        if bing_key:
            coders.append(("bing", bing_key))
        fLOG("geocoding 1", len(he))

        # test
        res = geocode(he, save_every=every, every=1, index=False,
                      encoding="utf-8", coders=coders, fLOG=fLOG)
        self.assertExists(every)
        # fLOG(res)
        out = os.path.join(temp, "geo.csv")
        res.to_csv(out, sep="\t", encoding="utf-8", index=False)
        res.to_excel(out + ".xlsx", index=False)
        fLOG("geocoding 2", len(res))
        res = geocode(he, save_every=every, every=1, index=False,
                      encoding="utf-8", coders=coders, fLOG=fLOG)
        self.assertExists(every)
        fLOG(res)


if __name__ == "__main__":
    unittest.main()
