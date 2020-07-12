# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)
"""
import os
import unittest
import pandas
from pyquickhelper.pycode import ExtTestCase, get_temp_folder
from actuariat_python.faq.faq_pandas import read_csv_from_excel
from actuariat_python.faq.faq_python import instruction_pass


class TestFaqPandas(ExtTestCase):

    def test_read_csv(self):
        temp = get_temp_folder(__file__, 'temp_read_csv')
        dest = os.path.join(temp, "dd.csv")
        df = pandas.DataFrame([{'a': 6}])
        df.to_csv(dest, index=False)
        df2 = read_csv_from_excel(dest)
        self.assertEqualDataFrame(df, df2)

    def test_instruction_pass(self):
        instruction_pass()


if __name__ == "__main__":
    unittest.main()
