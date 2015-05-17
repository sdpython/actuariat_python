"""
@file
@brief Various function to download data about population
"""

import pandas
from .data_exception import DataFormatException


def population_france_2015(url="http://www.insee.fr/fr/ffc/figure/ccc.xls", sheetname=0):
    """
    download the data for the French population from INSEE website

    @param      url             url
    @param      sheetname       sheet index
    @return                     DataFrame

    The sheet index is 0 for the all France, 1 for metropolitean France.
    The last row aggregates multiple ages ``1914 ou avant``, they will remain
    aggregated but the label will be changed to 1914. ``100 ou plus``is replaced by 100.
    """
    df = pandas.read_excel(url, sheetname=sheetname)
    col = df.columns[0]
    cp = df[df[col] == 2014]
    if len(cp) == 0:
        raise DataFormatException(
            "unable to find 2014 in table at url: " + url)
    if len(cp) != 1:
        raise DataFormatException(
            "too many values 2014 in table at url: " + url)
    ind = cp.index[0]
    table = df.ix[ind:, :5].copy()
    table.columns = ["naissance", "age", "hommes", "femmes", "ensemble"]
    table["naissance"] = table.apply(lambda r: r["naissance"] if isinstance(r["naissance"], int) else
                                     r["naissance"].replace(" ou avant", ""), axis=1)
    table["age"] = table.apply(lambda r: r["age"] if isinstance(r["age"], int) else
                               r["age"].replace(" ou plus", ""), axis=1)
    for c in table.columns:
        table[c] = table[c].astype(int)
    return table
