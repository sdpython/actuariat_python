#-*- coding: utf-8 -*-
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

    By default, the data is coming from `INSEE, Population française 2015 <http://www.insee.fr/fr/themes/tableau.asp?ref_id=ccc>`_.
    """
    df = pandas.read_excel(url, sheetname=sheetname)
    col = df.columns[0]
    cp = df[df[col] == 2014]
    if len(cp) == 0:
        raise DataFormatException(
            "unable to find 2014 (year) in table at url: " + url)
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


def table_mortalite_france_00_02(homme="http://www.institutdesactuaires.com/docs/2015130807_TH0002.xlsx",
                                 femme="http://www.institutdesactuaires.com/docs/2015130807_TF0002.xlsx"):
    """
    Download mortality table for France assuming they
    are available in Excel format.

    @param      homme       table for men
    @param      femme       table for women
    @return                 DataFrame

    The final DataFrame merges both sheets.
    By default, the data is coming from
    `Institut des Actuaires: Reférences de mortalité <http://www.institutdesactuaires.com/gene/main.php?base=314>`_.
    """
    dfh = pandas.read_excel(homme)
    dff = pandas.read_excel(femme)
    df = dfh.merge(dff, on="Age")
    df.columns = ["Age", "Homme", "Femme"]
    return df.dropna().reset_index(drop=True)


def fecondite_france(url="http://www.insee.fr/fr/ffc/figure/bilandemo2.xls"):
    """
    download fecondity table for France (Excel format)

    @param      url     source (url or file)
    @return             DataFrame

    By default, the data is coming from
    `INSEE: Fécondité selon l'âge détaillé de la mère <http://www.insee.fr/fr/themes/tableau.asp?reg_id=0&ref_id=bilandemo2>`_.
    """
    df = pandas.read_excel(url)
    col = df.columns[0]
    cp = df[df[col] == 15]
    if len(cp) == 0:
        raise DataFormatException(
            "unable to find 15 (age) in table at url: " + url)
    if len(cp) != 1:
        raise DataFormatException(
            "too many values 15 in table at url: " + url)
    cpe = df[df[col] == 50]
    if len(cpe) == 0:
        raise DataFormatException(
            "unable to find 50 (age) in table at url: " + url)
    if len(cpe) != 1:
        raise DataFormatException(
            "too many values 50 in table at url: " + url)
    ind = cp.index[0]
    ind2 = cpe.index[0]
    table = df.ix[ind:ind2, :3].copy()
    table.columns = ["age", "2004", "2014"]
    for c in table.columns:
        table[c] = table[c].astype(float)
    return table
