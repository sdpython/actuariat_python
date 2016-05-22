#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
"""

import sys
import os
import unittest


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
from pyquickhelper.pycode import add_missing_development_version


class TestElectionsNotebookCheck(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pyensae", "pymyinstall", "pyrsslocal"], __file__,
                                        hide=__name__ == "__main__")
        from src.actuariat_python.data import elections_presidentielles as skip__

    def test_elections_notebook(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.actuariat_python.data import elections_presidentielles
        dict_df = elections_presidentielles(local=True, agg="dep")
        fLOG(len(dict_df["dep1"]), len(dict_df["dep2"]))

        def cleandep(s):
            if isinstance(s, str):
                r = s.lstrip('0')
            else:
                r = str(s)
            return r

        fLOG("*")
        dict_df["dep1"]["Code du département"] = dict_df["dep1"]["Code du département"].apply(cleandep)
        fLOG("*")
        dict_df["dep2"]["Code du département"] = dict_df["dep2"]["Code du département"].apply(cleandep)
        fLOG("-------------", dict_df["dep1"][["Code du département"]].dtypes)
        fLOG(dict_df["dep1"].head()["Code du département"])
        fLOG("-------------", dict_df["dep2"][["Code du département"]].dtypes)
        fLOG(dict_df["dep2"].head()["Code du département"])
        fLOG("-------------")
        deps = dict_df["dep1"].merge(dict_df["dep2"], on="Code du département",
                                     suffixes=("T1", "T2"))
        fLOG(len(deps))
        assert len(deps) > 10
        assert len(deps) < 110
        deps["rHollandeT1"] = deps['François HOLLANDE (PS)T1'] / (deps["VotantsT1"] - deps["Blancs et nulsT1"])
        fLOG(len(deps["rHollandeT1"]))
        deps["rSarkozyT1"] = deps['Nicolas SARKOZY (UMP)T1'] / (deps["VotantsT1"] - deps["Blancs et nulsT1"])
        fLOG(len(deps["rSarkozyT1"]))
        deps["rNulT1"] = deps["Blancs et nulsT1"] / deps["VotantsT1"]
        deps["rHollandeT2"] = deps["François HOLLANDE (PS)T2"] / (deps["VotantsT2"] - deps["Blancs et nulsT2"])
        deps["rSarkozyT2"] = deps['Nicolas SARKOZY (UMP)T2'] / (deps["VotantsT2"] - deps["Blancs et nulsT2"])
        deps["rNulT2"] = deps["Blancs et nulsT2"] / deps["VotantsT2"]
        data = deps[["Code du département", "Libellé du départementT1",
                     "VotantsT1", "rHollandeT1", "rSarkozyT1", "rNulT1",
                     "VotantsT2", "rHollandeT2", "rSarkozyT2", "rNulT2"]]
        fLOG(data.shape)
        assert len(data) > 10


if __name__ == "__main__":
    unittest.main()
