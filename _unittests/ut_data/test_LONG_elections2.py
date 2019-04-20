# -*- coding: utf-8 -*-
"""
@brief      test log(time=5s)
"""
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version, get_temp_folder


class TestElections2(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pyrsslocal"], __file__)

    def test_elections_2012_bureau_vote(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_legislatives_bureau_vote
        temp = get_temp_folder(__file__, "temp_elections_bureau_vote")
        dfs = elections_legislatives_bureau_vote(
            fLOG=fLOG, folder=temp, source="xd")
        fLOG(type(dfs))
        fLOG(list(dfs.keys()))
        self.assertEqual(len(dfs), 2)
        assert "T1" in dfs
        assert "T2" in dfs
        assert isinstance(dfs["T1"], pandas.DataFrame)

    def test_elections_2012_contours(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_legislatives_circonscription_geo
        temp = get_temp_folder(__file__, "temp_elections_contour")
        dfs = elections_legislatives_circonscription_geo(
            fLOG=fLOG, folder=temp, source="xd")
        assert isinstance(dfs, pandas.DataFrame)
        self.assertEqual(dfs.shape, (577, 6))

    def test_elections_vote_places_geo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_vote_places_geo
        temp = get_temp_folder(__file__, "temp_elections_vote_places_geo")
        dfs = elections_vote_places_geo(
            fLOG=fLOG, folder=temp, source="xd")
        assert isinstance(dfs, pandas.DataFrame)
        assert len(dfs) > 10000
        exp = ['address', 'city', 'n', 'place', 'zip',
               'full_address', 'latitude', 'longitude', 'geo_address']
        self.assertEqual(list(dfs.columns), exp)


if __name__ == "__main__":
    unittest.main()
