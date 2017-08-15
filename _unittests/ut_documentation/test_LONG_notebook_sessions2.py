#-*- coding: utf-8 -*-
"""
@brief      test log(time=280s)
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
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut


class TestLONGNotebookPopulation2(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "pyrsslocal", "mlstatpy",
             "jyquickhelper"], __file__, hide=True)

    def test_notebook_population(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()

        from src.actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
        temp = get_temp_folder(__file__, "temp_sessions2")
        keepnote = [_ for _ in ls_notebooks(
            "sessions") if "seance6_graphes_ml_enonce" in _]
        self.assertTrue(len(keepnote) > 0)
        for k in keepnote:
            fLOG(k)
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.actuariat_python)


if __name__ == "__main__":
    unittest.main()
