# -*- coding: utf-8 -*-
"""
@brief      test log(time=50s)
"""
import sys
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut
import actuariat_python


class TestLONGNotebookInternet(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "pyrsslocal", "mlstatpy",
             "jyquickhelper"], __file__, hide=True)

    def test_notebook_internet(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fix_tkinter_issues_virtualenv()

        if "travis" in sys.executable:
            # matplotlib is still failing
            warnings.warn(
                "travis, unable to test TestNotebookInternet.test_notebook_internet")
            return

        from actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook
        from mlstatpy.data.wikipedia import download_pageviews
        self.assertTrue(download_pageviews)
        temp = get_temp_folder(__file__, "temp_internet")
        keepnote = [_ for _ in ls_notebooks(
            "internet") if "wikipedia_stats_correction" not in _]
        self.assertTrue(len(keepnote) > 0)
        for k in keepnote:
            fLOG(k)
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: True,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=actuariat_python)


if __name__ == "__main__":
    unittest.main()
