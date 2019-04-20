# -*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import add_missing_development_version


class TestElections(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pyensae", "pymyinstall", "pyrsslocal"], __file__,
                                        hide=__name__ == "__main__")

    def test_elections_2012_local(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_presidentielles_local_files
        res = elections_presidentielles_local_files(load=False)
        self.assertEqual(len(res), 2)
        res = elections_presidentielles_local_files(load=True)
        assert isinstance(res, dict)
        self.assertEqual(len(res), 2)
        for v in res.values():
            self.assertEqual(v.shape[0], 577)

    def test_elections_2012(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_presidentielles
        dfs = elections_presidentielles(local=True)
        fLOG(type(dfs))
        fLOG(list(dfs.keys()))
        assert len(dfs) > 0
        dfs = elections_presidentielles()
        fLOG(type(dfs))
        fLOG(list(dfs.keys()))
        assert len(dfs) > 0

    def test_elections_2012_departements(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.data import elections_presidentielles
        dfs = elections_presidentielles(local=True, agg="dep")
        fLOG(type(dfs))
        fLOG(list(dfs.keys()))
        self.assertEqual(dfs["dep1"].shape, (107, 17))
        self.assertEqual(dfs["dep2"].shape, (107, 9))


if __name__ == "__main__":
    unittest.main()
