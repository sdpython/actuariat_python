# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.

"""
import pandas


def read_csv_from_excel(filename, sep="\t", encoding="iso-8859-1"):
    """
    Read a file stored in CSV format from Excel.
    
    @param      filename        filename
    @param      sep             column separator
    @param      encoding        default encoding
    @return                     DataFrame


    @FAQ(pandas___Lire un fichier CSV enregistré avec Excel)

    Excel utilise un encoding par défaut qui est souvent *iso-8859-1*, c'est pourquoi
    la fonction *pandas.read_csv* génère parfois des erreurs lorsque le texte contient des accents.
    Il faut lui donner plus d'information sur le contenu :
    
    @code
    df2 = pandas.read_csv("base.csv", sep=";" , encoding="iso-8859-1", low_memory=False)
    @endcode

    Le ``low_memory=False`` est suggéré par un warning de pandas.
    On peut aussi essayer la version de *read_csv* implémentée en python (en non C).
    Elle est moins rapide mais gère plus de cas (il faut lire le code 
    pour comprendre pourquoi car la documentation est avare en informations
    à ce sujet).

    @code
    df2 = pandas.read_csv("base.csv", sep=";" , engine="python")
    @endcode
    
    @endFAQ
    """
    try:
        return pandas.read_csv(filename, sep=sep, encoding=encoding, low_memory=False)
    except:
        return pandas.read_csv(filename, sep=sep, encoding=encoding, engine="python")
