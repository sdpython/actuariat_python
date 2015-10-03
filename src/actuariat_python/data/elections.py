#-*- coding: utf-8 -*-
"""
@file
@brief Various function to download data about elections
"""
import pandas


def elections_presidentielles(url="http://static.data.gouv.fr/ff/e9c9483d39e00030815089aca1e2939f9cb99a84b0136e43056790e47bb4f0.xls"):
    """
    download the data for the French elections from data.gouv.fr

    @param      url             url
    @return                     dictionaries of DataFrame

    The default url comes from
    `Election présidentielle 2012 - Résultats <https://www.data.gouv.fr/fr/datasets/election-presidentielle-2012-resultats-572124/>`_.
    You can get more at
    `Elections présidentielles 1965-2012 <https://www.data.gouv.fr/fr/datasets/elections-presidentielles-1965-2012-1/>`_.
    """
    df = pandas.read_excel(url, sheetname=None)
    return df
