#-*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""

import sys
import os
import unittest
import re

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
    import pyquickhelper
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
    import pyquickhelper

from pyquickhelper import fLOG, get_temp_folder
from src.actuariat_python.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_notebook


class TestNotebookMortalite(unittest.TestCase):

    def test_notebook_mortalite(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_mortalite")
        keepnote = ls_notebooks("mortalite")
        assert len(keepnote) > 0
        res = execute_notebooks(temp, keepnote,
                                lambda i, n: "deviner" not in n,
                                fLOG=fLOG,
                                clean_function=clean_function_notebook)
        assert len(res) > 0
        fails = [(os.path.split(k)[-1], v[0], v[1])
                 for k, v in sorted(res.items()) if not v[0]]
        for f in fails:
            fLOG(f)
        if len(fails) > 0:
            raise fails[0][1][-1]
        for k, v in sorted(res.items()):
            fLOG("final", os.path.split(k)[-1], v[0], v[1])

if __name__ == "__main__":
    unittest.main()
