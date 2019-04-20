# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv


class TestLONGinit(unittest.TestCase):

    def test_long_init(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fLOG("do nothing")
        fix_tkinter_issues_virtualenv()


if __name__ == "__main__":
    unittest.main()
