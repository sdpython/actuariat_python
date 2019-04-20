# -*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
"""
import os
import unittest
import shutil
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version
from pyquickhelper.ipythonhelper import execute_notebook_list_finalize_ut
import actuariat_python


class TestNotebookDecouvrte(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(
            ["pyensae", "pymyinstall", "pymmails", "pyrsslocal", "mlstatpy",
             "jyquickhelper"], __file__, hide=True)

    def test_notebook_decouverte(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        from actuariat_python.automation.notebook_test_helper import clean_function_notebook
        temp = get_temp_folder(__file__, "temp_decouverte")
        keepnote = [_ for _ in ls_notebooks("decouverte")]
        self.assertTrue(len(keepnote) > 0)

        # copy data
        folder = os.path.dirname(keepnote[0])
        data = [os.path.join(folder, "UN_Data.csv")]
        for dt in data:
            shutil.copy(dt, temp)

        # run the notebooks
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: True,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=actuariat_python)


if __name__ == "__main__":
    unittest.main()
