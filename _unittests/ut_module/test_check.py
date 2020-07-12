"""
@brief      test log(time=0s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from actuariat_python import check, _setup_hook


class TestModule(ExtTestCase):
    """Test style."""

    def test_check(self):
        check()
        _setup_hook()


if __name__ == "__main__":
    unittest.main()
