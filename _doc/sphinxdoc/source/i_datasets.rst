
.. _l-datasets:

===============
Jeux de données
===============

Données non pretraitées
=======================

Certains jeux de données ont été incluses dans le module. La première raison est
que les sites qui les fournissent fonctionnent par intermittence bien que ces données soient publiques.

Elections
+++++++++

Ce jeux regroupes l'ensembles des élections depuis le site
`Elections présidentielles 1965-2012 <https://www.data.gouv.fr/fr/datasets/elections-presidentielles-1965-2012-1/>`_.
La fonction :func:`elections_presidentielles <actuariat_python.data.elections.elections_presidentielles>`
retourne le résultat des élections présidentielles de 2012 par circonscription.
Le module :mod:`elections <actuariat_python.data.elections>` regroupe plusieurs fonctions
qui téléchargent des données qu'elles retournent sous forme de dataframe.

Données prétraitées depuis un notebook
======================================

Certaines données nécessitent d'être prétraitées avant de pouvoir être utilisées et cela
nécessite parfois plusieurs lignes de codes. Certaines fonctions ont été ajoutées à ce module
afin de pouvoir facilement récupérer ces données, plus ou moins longues selon
les données. C'est une partie incontournable et rébarbative. Pour aller plus vite, on part
d'un code existant qu'on modifie au besoin.
Les notebooks suivants illustrent comment utiliser ce module pour
obtenir ces jeux de données.

.. toctree::
    :maxdepth: 1

    Données sur la population françaises <notebooks/population_recuperation_donnees>
    Localisation des bureaux de vote <notebooks/election_carte_electorale>
