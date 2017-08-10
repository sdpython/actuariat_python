#-*- coding: utf-8 -*-
"""
@brief      test log(time=233s)
"""

import sys
import os
import unittest
import shutil

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
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, is_travis_or_appveyor


class TestNotebookSession(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pyrsslocal", "mlstatpy", "jyquickhelper",
             "ensae_teaching_cs"], __file__)

    def test_notebook_session(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()

        from src.actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook, unittest_raise_exception_notebook
        temp = get_temp_folder(__file__, "temp_sessions")
        keepnote = [_ for _ in ls_notebooks(
            "sessions") if "seance5_approche_fonctionnelle_enonce" not in _ and
            "seance6_graphes_ml_enonce" not in _ and "election_carte_electorale_correction" not in _ and
            "seance6_graphes_correction" not in _ and "seance6_graphes_enonce" not in _ and "ways" not in _]
        if is_travis_or_appveyor():
            keepnote = [
                _ for _ in keepnote if "election_carte_electorale" not in _]
        self.assertTrue(len(keepnote) > 0)
        for k in keepnote:
            fLOG(k)

        # copy data
        fold = os.path.dirname(keepnote[0])
        files = [os.path.join(fold, "pop-totale-france.txt")]
        for name in files:
            shutil.copy(name, temp)
        data_tem = os.path.join(temp, "data")
        if not os.path.exists(data_tem):
            os.mkdir(data_tem)
        files = [os.path.join(fold, "data", "housing.data"),
                 os.path.join(fold, "data", "housing.names"),
                 os.path.join(fold, "data", "multiTimeline.csv"), ]
        for name in files:
            shutil.copy(name, data_tem)

        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        unittest_raise_exception_notebook(res, fLOG)


if __name__ == "__main__":
    unittest.main()
