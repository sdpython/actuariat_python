

.. blogpost::
    :title: Différence entre numpy et pandas
    :keywords: sql, matrice
    :date: 2015-06-06
    :categories: calcul matriciel, modules
    
    Pourquoi deux modules alors qu'ils semblent tous deux
    manipuler des matrices ? Dans le cas de 
    `pandas <http://pandas.pydata.org/>`_, ce ne sont pas tout-à-fait
    des matrices mais des tables de données : la même 
    table peut contenir différentes types de données, des
    nombres, des chaînes de caractères, des booléens, des dates...
    Les données se manipulent comme des bases de données et 
    les `Dataframe <http://pandas.pydata.org/pandas-docs/version/0.16.1/generated/pandas.DataFrame.html>`_
    de pandas sont optimisés pour ça. Chaque colonne porte un nom.
    
    `numpy <http://www.numpy.org/>`_ propose des 
    `matrices <http://wiki.scipy.org/Tentative_NumPy_Tutorial>`_ à une ou plusieurs
    dimensions optimisées pour le calcul matriciel. Ces matrices ne contiennent que des nombres et 
    tous du même type.
    
    Pour faire un produit matriciel, on choisit numpy.
    Pour faire une jointure de table, on choisit pandas.
    