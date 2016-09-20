#-*- coding: utf-8 -*-
"""
@brief      test log(time=20s)
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
from pyquickhelper.pycode import add_missing_development_version, get_temp_folder


class TestBureauVote(unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pyensae", "pymyinstall", "pyrsslocal"], __file__,
                                        hide=__name__ == "__main__")
        from src.actuariat_python.data import elections_presidentielles as skip__

    def test_elections_vote_place_address(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from src.actuariat_python.data import elections_vote_place_address
        temp = get_temp_folder(__file__, "temp_elections_vote_place_address")
        res = elections_vote_place_address(folder=temp, fLOG=fLOG)
        fLOG(res.shape)
        self.assertEqual(res.shape[1], 5)
        assert len(res) > 100
        fLOG(res.head())
        out = os.path.join(temp, "bureau.txt")
        res.to_csv(out, sep="\t", encoding="utf-8", index=False)
        res.to_excel(out + ".xlsx", index=False)

    def test_regex(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.actuariat_python.data.elections import _elections_vote_place_address_patterns
        from src.actuariat_python.data.elections import html_to_text
        datas = [os.path.join(os.path.abspath(os.path.dirname(
            __file__)), "data", "bv0%d.txt") % i for i in range(1, 6)]
        for data in datas:
            with open(data, "r", encoding="iso-8859-1") as f:
                content = f.read().lower()
            content = html_to_text(content)
            content0 = content
            content = content.replace("\n", " ")
            regex = [re.compile(_)
                     for _ in _elections_vote_place_address_patterns]
            res = []
            for i, reg in enumerate(regex):
                fa = reg.findall(content)
                res += [(i, _) for _ in fa]
            if len(res) < 15:
                raise Exception(content0)
            fLOG("data", os.path.split(data)[-1], len(res))


if __name__ == "__main__":
    unittest.main()
