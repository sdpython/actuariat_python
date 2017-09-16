#-*- coding: utf-8 -*-
"""
@brief      test log(time=201s)
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
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut


class TestNotebookSession4(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "pyrsslocal", "mlstatpy",
             "jyquickhelper"], __file__, hide=True)
        fix_tkinter_issues_virtualenv()
        self.fLOG = fLOG

    def a_test_notebook_session(self, name):
        from src.actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
        fLOG = self.fLOG
        temp = get_temp_folder(__file__, "temp_sessions")
        keepnote = [_ for _ in ls_notebooks(
            "sessions") if "seance5_approche_fonctionnelle_enonce" not in _ and
            "seance6_graphes_ml_enonce" not in _ and "election_carte_electorale_correction" not in _ and
            "seance6_graphes_correction" not in _ and "seance6_graphes_enonce" not in _ and "ways" not in _]
        if is_travis_or_appveyor():
            keepnote = [
                _ for _ in keepnote if "election_carte_electorale" not in _]
        if name is not None:
            keepnote = list(filter(lambda n: name in n, keepnote))
        if len(keepnote) == 0:
            return
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
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.actuariat_python)    

    def test_notebook_session5(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_session(
            "seance5_approche_fonctionnelle_correction.ipynb")

    def test_notebook_session6(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_session(
            "seance5_cube_multidimensionnel_correction.ipynb")


if __name__ == "__main__":
    unittest.main()
