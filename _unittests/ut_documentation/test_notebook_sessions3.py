# -*- coding: utf-8 -*-
"""
@brief      test log(time=202s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, is_travis_or_appveyor
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut
import actuariat_python


class TestNotebookSession3(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "pyrsslocal", "mlstatpy",
             "jyquickhelper"], __file__, hide=True)
        fix_tkinter_issues_virtualenv()

    def a_test_notebook_session(self, name):
        from actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
        temp = get_temp_folder(__file__, "temp_sessions_" + name.split('.')[0])
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
        for name_ in files:
            shutil.copy(name_, temp)
        data_tem = os.path.join(temp, "data")
        if not os.path.exists(data_tem):
            os.mkdir(data_tem)
        files = [os.path.join(fold, "data", "housing.data"),
                 os.path.join(fold, "data", "housing.names"),
                 os.path.join(fold, "data", "multiTimeline.csv"), ]
        for name_ in files:
            shutil.copy(name_, data_tem)

        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=actuariat_python)

    def test_notebook_session7(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_session(
            "seance5_cube_multidimensionnel_enonce.ipynb")

    def test_notebook_session8(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_session(
            "seance5_sql_multidimensionnelle_correction.ipynb")

    def test_notebook_session9(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_session(
            "seance5_sql_multidimensionnelle_enonce.ipynb")

    def test_notebook_session10(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        self.a_test_notebook_session("seance6_graphes_ml_correction.ipynb")


if __name__ == "__main__":
    unittest.main()
