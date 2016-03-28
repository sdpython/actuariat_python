#-*- coding: utf-8 -*-
"""
@file
@brief Various function to download data about elections
"""
import pandas
import os
from urllib.error import HTTPError, URLError
from .data_exceptions import DataNotAvailableError


def elections_presidentielles_local_files(load=False):
    """
    return the list of files included in this module about French elections

    @param      load        True: load the data
    @return                 list of local files

    If the data is loaded, the function returns a dictionary of dataframe,
    one per round.
    """
    this = os.path.dirname(__file__)
    data = os.path.abspath(os.path.join(this, "data_elections"))
    res = [os.path.join(data, "cdsp_presi2012t1_circ.xls"),
           os.path.join(data, "cdsp_presi2012t2_circ.xls")]
    for r in res:
        if not os.path.exists(r):
            raise FileNotFoundError(r)

    if not load:
        return res
    else:
        df1 = pandas.read_excel(res[0], sheetname=1)
        df2 = pandas.read_excel(res[1], sheetname=1)
        return dict(t1=df1, t2=df2)


def elections_presidentielles(url=None, local=False):
    """
    download the data for the French elections from data.gouv.fr

    @param      url             url (None for default value)
    @param      local           prefer local data instead of remote
    @return                     dictionaries of DataFrame (one entry for each round)

    The default url comes from
    `Elections présidentielle 2012 - Résultats <https://www.data.gouv.fr/fr/datasets/election-presidentielle-2012-resultats-572124/>`_.
    You can get more at
    `Elections présidentielles 1965-2012 <https://www.data.gouv.fr/fr/datasets/elections-presidentielles-1965-2012-1/>`_.

    If url is None, we pull some data from folder
    :ref:`data/election <l-data-elections>`.
    """
    if local:
        return elections_presidentielles_local_files(load=True)
    else:
        if url is None:
            url = "http://static.data.gouv.fr/ff/e9c9483d39e00030815089aca1e2939f9cb99a84b0136e43056790e47bb4f0.xls"
            url0 = None
        else:
            url0 = url
        try:
            df = pandas.read_excel(url, sheetname=None)
            return df
        except (HTTPError, URLError, TimeoutError) as e:
            if url0 is None:
                return elections_presidentielles_local_files(load=True)
            else:
                raise DataNotAvailableError(
                    "unable to get data from " + url) from e
