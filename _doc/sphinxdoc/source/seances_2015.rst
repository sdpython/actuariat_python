

.. _l-seances-2015:

Séances 2015
============


notebooks
+++++++++

.. toctree::
    :maxdepth: 1

    notebooks/seance4_projection_population_enonce
    
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
    



plan prévisionnel
+++++++++++++++++

#. Septembre : 
    * Machine Learning en Python avec scikit-learn
    * Chaînes de traitement
        * data transformers
        * modèles (classifiers, ....)
        * évaluation (ROC, :math:`R^2`, ...)
    * Types de modèles
        * regressors
        * clustering
        * dimensionality reduction (PCA)
        * système de recommandation
        * traitement du langage (NLTK), représentation des mots (word2vec)
    * Sélection de modèles
        * cross validation
    * Un exemple
    * Programmer ou workflow de données (Orange)
#. Octobre
    * Visualisation poussées, matplotlib, ggplot, bohek, mpld3
    * Graph avec `igraph <http://igraph.org/>`_
    * Autres environnements
        * Spyder
        * PyCharm
    * Customiser son environnement (commandes magiques)
    * R dans un notebook (IPython 3 ==> Jupyter)
    * R et Python dans un notebook
    * Présentation du problème de la séance suivante afin que les stagiaires puissent réfléchir en amont.
#. Novembre
    * Implémenter la simulation d'un régime de retraite complémentaire à partir de sa population.
      On suppose connu son fichier client, on prend quelques hypothèses de rendements, taux d'entrées, ...
      C'est une simulation micro économique : on fait évoluer la population année après année.
    * Définition des règles qui régissent l'évolution du système
    * Choix des structures de données
    * Implémentation des règles
    * Simulation
    * Graphes qui retracent l'évolution de variables exhaustive (réserves, ...)