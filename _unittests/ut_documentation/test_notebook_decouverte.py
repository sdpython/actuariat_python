#-*- coding: utf-8 -*-
"""
@brief      test log(time=10s)
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


class TestNotebookDecouvrte(unittest.TestCase):

    def setUp(self):
        "import dependencies"
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "pyrsslocal",
                                         "mlstatpy", "jyquickhelper"], __file__, hide=True)

    def test_notebook_decouverte(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        from src.actuariat_python.automation.notebook_test_helper import clean_function_notebook, unittest_raise_exception_notebook
        temp = get_temp_folder(__file__, "temp_decouverte")
        keepnote = [_ for _ in ls_notebooks("decouverte")]
        assert len(keepnote) > 0
        folder = os.path.dirname(keepnote[0])
        data = [os.path.join(folder, "UN_Data.csv")]
        for dt in data:
            shutil.copy(dt, temp)
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: True,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        unittest_raise_exception_notebook(res, fLOG)


if __name__ == "__main__":
    unittest.main()
