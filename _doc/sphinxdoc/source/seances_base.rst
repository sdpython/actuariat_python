

.. _l-seances-base:

Séances 2015
============


notebooks
+++++++++

.. toctree::
    :maxdepth: 1
    :hidden:

    notebooks/seance4_projection_population_enonce
    notebooks/seance4_projection_population_correction
    notebooks/seance5_sql_multidimensionnelle_enonce
    notebooks/seance5_sql_multidimensionnelle_correction
    notebooks/seance5_cube_multidimensionnel_enonce
    notebooks/seance5_cube_multidimensionnel_correction
    notebooks/seance5_approche_fonctionnelle_enonce
    notebooks/seance5_cube_multidimensionnel_correction
    
#. :ref:`Simulation d'une population <seance4projectionpopulationenoncerst>` (:ref:`correction <seance4projectionpopulationcorrectionrst>`)
#. :ref:`SQL et grosses base de données <seance5sqlmultidimensionnelleenoncerst>` (:ref:`correction <seance5sqlmultidimensionnellecorrectionrst>`)
#. :ref:`Cube multidimensionnel <seance5cubemultidimensionnelenoncerst>` (:ref:`correction <seance5cubemultidimensionnelcorrectionrst>`)
#. :ref:`Approche fonctionnelle <seance5approchefonctionnelleenoncerst>` (:ref:`correction <seance5approchefonctionnellecorrectionrst>`)

    
Jeux de données
+++++++++++++++

Certaines données nécessitent d'être prétraitées avant de pouvoir être utilisées et cela
nécessite parfois plusieurs lignes de codes. Certaines fonctions ont été ajoutées à ce module
afin de pouvoir facilement récupérer ces données, plus ou moins longues selon
les données. C'est une partie incontournable et rébarbative. Pour aller plus vite, on part
d'un code existant qu'on modifie au besoin. 
Les notebooks suivants illustrent comment utiliser ce module pour
obtenir ces jeux de données.

.. toctree::
    
    notebooks/population_recuperation_donnees
    

Bibliographie
+++++++++++++

**articles, blogs**


* `Xray + Dask: Out-of-Core, Labeled Arrays in Python <http://continuum.io/blog/xray-dask>`_
* `A thorough guide to SQLite database operations in Python <http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html>`_


plan prévisionnel
+++++++++++++++++

#. Octobre
    * visualisation
#. Novembre
    * Implémenter la simulation d'un régime de retraite complémentaire à partir de sa population.
      On suppose connu son fichier client, on prend quelques hypothèses de rendements, taux d'entrées, ...
      C'est une simulation micro économique : on fait évoluer la population année après année.
    * Définition des règles qui régissent l'évolution du système
    * Choix des structures de données
    * Implémentation des règles
    * Simulation
    * Graphes qui retracent l'évolution de variables exhaustive (réserves, ...)