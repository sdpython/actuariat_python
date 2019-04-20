# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, add_missing_development_version
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut
import actuariat_python


class TestNotebookExamen(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "pyrsslocal", "mlstatpy",
             "jyquickhelper"], __file__, hide=True)

    def test_notebook_examen(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()
        from actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
        temp = get_temp_folder(__file__, "temp_examen")
        keepnote = ls_notebooks("examen")
        self.assertTrue(len(keepnote) > 0)
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG, clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=actuariat_python)


if __name__ == "__main__":
    unittest.main()
