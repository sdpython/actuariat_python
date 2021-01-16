# -*- coding: utf-8 -*-
"""
@brief      test log(time=1061s)
"""
import sys
import unittest
import warnings
from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut
import actuariat_python


class TestLONGNotebookPopulationS6Correction(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "pyrsslocal", "mlstatpy",
             "jyquickhelper"], __file__, hide=True)

    def test_long_long_notebook_population_s6_correction(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()
        from actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook

        if "travis" in sys.executable:
            # matplotlib is still failing
            warnings.warn(
                "travis, unable to test TestNotebookPopulation.test_notebook_sessions")
            return

        temp = get_temp_folder(__file__, "temp_sessions_long_long")
        keepnote = [_ for _ in ls_notebooks(
            "sessions") if "seance6_graphes_correction"]
        self.assertTrue(len(keepnote) > 0)
        clog = CustomLog(temp)
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG, clean_function=clean_function_notebook,
                                detailed_log=clog)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=actuariat_python)


if __name__ == "__main__":
    unittest.main()
