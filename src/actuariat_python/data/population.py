#-*- coding: utf-8 -*-
"""
@file
@brief Various function to download data about population
"""
import numpy
import pandas
import gzip
import os
from pyquickhelper import noLOG
import pyensae
from .data_exception import DataFormatException


def population_france_2015(url="http://www.insee.fr/fr/ffc/figure/ccc.xls",
                           sheetname=0, year=2015):
    """
    download the data for the French population from INSEE website

    @param      url             url
    @param      sheetname       sheet index
    @param      year            last year to find
    @return                     DataFrame

    The sheet index is 0 for the all France, 1 for metropolitean France.
    The last row aggregates multiple ages ``1914 ou avant``, they will remain
    aggregated but the label will be changed to 1914. ``100 ou plus`` is replaced by 100.

    By default, the data is coming from `INSEE, Population française 2015 <http://www.insee.fr/fr/themes/tableau.asp?ref_id=ccc>`_.
    """
    df = pandas.read_excel(url, sheetname=sheetname)
    col = df.columns[0]
    cp = df[df[col] == year]
    if len(cp) == 0:
        raise DataFormatException(
            "unable to find {0} (year) in table at url: {1}".format(year, url))
    if len(cp) != 1:
        raise DataFormatException(
            "too many values {0} in table at url: {1}".format(year, url))
    ind = cp.index[0]
    table = df.ix[ind:, :5].copy()
    table.columns = ["naissance", "age", "hommes", "femmes", "ensemble"]
    table = table[(table.naissance != 'Champ : France y c. Mayotte.') &
                  table.naissance.apply(lambda s: "Source" not in str(s))].copy()
    table["naissance"] = table.apply(lambda r: r["naissance"] if isinstance(r["naissance"], int) else
                                     r["naissance"].replace(" ou avant", ""), axis=1)
    table["age"] = table.apply(lambda r: r["age"] if isinstance(r["age"], int) else
                               r["age"].replace(" ou plus", "") if isinstance(
                                   r["age"], str) else r["age"],
                               axis=1)
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
    df[col] = df.apply(lambda r: r[col] if isinstance(r[col], int) else
                       r[col].replace(" ou plus", "").replace(" ans", "") if isinstance(
        r[col], str) else r[col],
        axis=1)
    df = df[df[col].apply(lambda x: "0" <= x[0] <= "9" if isinstance(
        x, str) else (isinstance(x, int) or isinstance(x, float)))].copy()
    df[col] = df[col].astype(float)
    cp = df[df[col] == 15]
    if len(cp) == 0:
        ages = [str(_) for _ in set(df[col])]
        raise DataFormatException(
            "unable to find 15 (age) in table at url: {0}\n{1}".format(url, "\n".join(ages)))
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
    table.columns = ["age", "2005", "2015"]
    for c in table.columns:
        table[c] = table[c].astype(float)
    return table


def table_mortalite_euro_stat(url="http://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/",
                              name="demo_mlifetable.tsv.gz",
                              final_name="mortalite.txt",
                              whereTo=".",
                              stop_at=None,
                              fLOG=noLOG):
    """
    This function retrieves mortality table from `EuroStat <http://ec.europa.eu/eurostat/fr>`_ through
    `table de mortalité <http://www.data-publica.com/opendata/7098--population-et-conditions-sociales-table-de-mortalite-de-1960-a-2010>`_.

    @param      url         data source
    @param      name        data table name
    @param      final_name  the data is compressed, it needs to be uncompressed into a file,
                            this parameter defines its name
    @param      whereTo     data needs to be downloaded, location of this place
    @param      stop_at     the overall process is quite long, if not None, it only keeps the first rows
    @param      fLOG        logging function
    @return                 data_frame

    The function checks the file final_name exists.
    If it is the case, the data is not downloaded twice.

    The header contains a weird format as coordinates are separated by a comma::

        indic_de,sex,age,geo\time	2013 	2012 	2011 	2010 	2009

    We need to preprocess the data to split this information into columns.
    The overall process takes 4-5 minutes, 10 seconds to download (< 10 Mb),
    4-5 minutes to preprocess the data (it could be improved). The processed data
    contains the following columns::

        ['annee', 'valeur', 'age', 'age_num', 'indicateur', 'genre', 'pays']

    Columns *age* and *age_num* look alike. *age_num* is numeric and is equal
    to *age* except when *age_num* is 85. Everybody above that age fall into the same category.
    The table contains many indicators:

    * PROBSURV: Probabilité de survie entre deux âges exacts (px)
    * LIFEXP: Esperance de vie à l'âge exact (ex)
    * SURVIVORS: Nombre des survivants à l'âge exact (lx)
    * PYLIVED: Nombre d'années personnes vécues entre deux âges exacts (Lx)
    * DEATHRATE: Taux de mortalité à l'âge x (Mx)
    * PROBDEATH: Probabilité de décès entre deux âges exacts (qx)
    * TOTPYLIVED: Nombre total d'années personne vécues après l'âge exact (Tx)
    """
    if os.path.exists(final_name) and os.stat(final_name).st_size > 1e7:
        return final_name

    temp = final_name + ".remove.txt"
    if not os.path.exists(temp) or os.stat(temp).st_size < 1e7:
        local = pyensae.download_data(name, url=url, whereTo=whereTo)
        local = local[0] + ".gz"
        with gzip.open(local, 'rb') as f:
            file_content = f.read()
        content = str(file_content, encoding="utf8")
        with open(temp, "w", encoding="utf8") as f:
            f.write(content)

    def format_age(s):
        if s.startswith("Y_"):
            if s.startswith("Y_LT"):
                s = "YLT" + s[4:]
            elif s.startswith("Y_GE"):
                s = "YGE" + s[4:]
            else:
                raise SyntaxError(s)
        else:
            i = int(s.strip("Y"))
            return "Y%02d" % i

    def format_age_num(s):
        if s.startswith("Y_"):
            if s.startswith("Y_LT"):
                s = float(s.replace("Y_LT", ""))
            elif s.startswith("Y_GE"):
                s = float(s.replace("Y_GE", ""))
            else:
                raise SyntaxError(s)
        else:
            i = int(s.strip("Y"))
            return float(i)

    def format_value(s):
        if s.strip() == ":":
            return numpy.nan
        else:
            return float(s.strip(" eb"))

    fLOG("step 0, reading")
    dff = pandas.read_csv(temp, sep="\t", encoding="utf8")

    if stop_at is not None:
        fLOG("step 0, shortening")
        dfsmall = dff.head(n=stop_at)
        df = dfsmall
    else:
        df = dff

    fLOG("step 1, size=", df.shape)
    dfi = df.reset_index().set_index("indic_de,sex,age,geo\\time")
    dfi = dfi.drop('index', axis=1)
    dfs = dfi.stack()
    dfs = pandas.DataFrame({"valeur": dfs})

    fLOG("step 2, size=", dfs.shape)
    dfs["valeur"] = dfs["valeur"].astype(str)
    dfs["valeur"] = dfs["valeur"].apply(format_value)
    dfs = dfs[dfs.valeur >= 0].copy()
    dfs = dfs.reset_index()
    dfs.columns = ["index", "annee", "valeur"]

    fLOG("step 3, size=", dfs.shape)
    dfs["age"] = dfs["index"].apply(lambda i: format_age(i.split(",")[2]))
    dfs["age_num"] = dfs["index"].apply(
        lambda i: format_age_num(i.split(",")[2]))
    dfs["indicateur"] = dfs["index"].apply(lambda i: i.split(",")[0])
    dfs["genre"] = dfs["index"].apply(lambda i: i.split(",")[1])
    dfs["pays"] = dfs["index"].apply(lambda i: i.split(",")[3])

    fLOG("step 4")
    dfy = dfs.drop('index', axis=1)
    dfy.to_csv(final_name, sep="\t", encoding="utf8", index=False)
    return final_name
