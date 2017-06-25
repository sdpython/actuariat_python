
.. blogpost::
    :title: Machine Learning - session 6
    :keywords: python, machine learning
    :date: 2017-06-25
    :categories: session

    **Exercices**

    * Sélection de features
        * Comparaison des tests de coefficients pour un modèle linéaire
          `OLS <http://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html>`_,
          et des `features importance <http://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html>`_
        * Résultat au niveau d'une observation `treeinterpreter <https://github.com/andosa/treeinterpreter>`_
        * Données : `Housing <https://archive.ics.uci.edu/ml/datasets/housing>`_,
          `Forest Fire <https://archive.ics.uci.edu/ml/datasets/Forest+Fires>`_
    * Prédiction et séries temporelles
        * Comparaison d'un modèle `ARIMA <http://www.statsmodels.org/dev/generated/statsmodels.tsa.arima_model.ARIMA.html>`_
          et d'une `random forest <http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>`_
          avec les séries décalées
          `lagmat <http://www.statsmodels.org/0.8.0/generated/statsmodels.tsa.tsatools.lagmat.html>`_,
          `pandas.shift <https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.shift.html>`_
        * Données : `DowJones <https://archive.ics.uci.edu/ml/datasets/Dow+Jones+Index>`_,
          `Google Trends <https://trends.google.fr/trends/explore?q=live%20tennis>`_
        * Notebooks :
          `Timeseries et machine learning <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/notebooks/ml_timeseries_base.html>`_
    * Text
        * Comparer une `LDA <http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html>`_ avec
          `word2vec <https://radimrehurek.com/gensim/models/word2vec.html>`_ +
          `kmeans <http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html>`_
        * Données :
            * `tweets <https://github.com/sdpython/ensae_teaching_cs/tree/master/src/ensae_teaching_cs/data/data_web>`_
        * Notebooks :
            * `Texte et machine learning <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/notebooks/td2a_some_nlp.html>`_

    **Plan**

    * Modules
        * Classique
            * `pandas <http://pandas.pydata.org/>`_,
              `numpy <http://www.numpy.org/>`_,
              `scipy <https://www.scipy.org/>`_
            * `scikit-learn <http://scikit-learn.org/stable/>`_,
              `xgboost <https://xgboost.readthedocs.io/en/latest/>`_
            * `statsmodels <http://www.statsmodels.org/stable/index.html>`_,
            * `prince <https://github.com/MaxHalford/Prince>`_,
              `fbpca <http://fbpca.readthedocs.io/en/latest/>`_
            * `nltk <http://www.nltk.org/>`_,
              `gensim <https://radimrehurek.com/gensim/>`_
        * Extension
            * Extension de scikit-learn (`category_encoders <https://github.com/scikit-learn-contrib/categorical-encoding>`_, ...)
            * `imbalanced-learn <https://github.com/scikit-learn-contrib/imbalanced-learn>`_
            * `polylearn <https://github.com/scikit-learn-contrib/polylearn>`_,
              `lightfm <https://github.com/lyst/lightfm>`_
            * `edward <http://edwardlib.org/>`_
            * `pyflux <http://www.pyflux.com/>`_
            * interprétation d'une prédiction
              `treeinterpreter <https://github.com/andosa/treeinterpreter>`_
            * `pyfolio <https://github.com/quantopian/pyfolio>`_,
              `zipline  <http://www.zipline.io/>`_
            * `lda2vec <https://github.com/cemoody/lda2vec>`_,
              `spacy <https://spacy.io/>`_
        * Auto learning
            * `auto-sklearn <https://github.com/automl/auto-sklearn>`_
            * `TPOT <https://github.com/rhiever/tpot>`_
        * Graphes
            * Graphes (`ROC <https://fr.wikipedia.org/wiki/Courbe_ROC>`_,
              `plus de maths <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html>`_,
              `sklearn.metrics.roc_curve <http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_curve.html>`_)
            * `matplotlib <https://matplotlib.org/>`_,
              `seaborn <https://seaborn.pydata.org/>`_,
              `bokeh <http://bokeh.pydata.org/en/latest/>`_
        * Cartes
            * `basemap <https://matplotlib.org/basemap/>`_,
            * `shapely <https://pypi.python.org/pypi/Shapely>`_,
              `pyproj <https://pypi.python.org/pypi/pyproj>`_
        * Données cryptées
            * `cyphermed <https://github.com/rbost/ciphermed>`_
    * Revue des différents problèmes de machine learning
        * `Python pour un datascientist <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a.html#>`_
    * Texte
        * Aperçu de traitement du langage
          `Texte et machine learning <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/notebooks/td2a_some_nlp.html>`_
