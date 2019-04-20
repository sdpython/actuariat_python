# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version, get_temp_folder


class TestElectionsBugBureauVote(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pyensae", "pymyinstall", "pyrsslocal"], __file__,
                                        hide=__name__ == "__main__")

    def test_elections_legislatives_bureau_vote(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_legislatives_bureau_vote
        temp = get_temp_folder(
            __file__, "temp_elections_legislatives_bureau_vote")
        ds = elections_legislatives_bureau_vote(folder=temp)
        ks = list(sorted(ds.keys()))
        self.assertEqual(ks, ['T1', 'T2'])


if __name__ == "__main__":
    unittest.main()
