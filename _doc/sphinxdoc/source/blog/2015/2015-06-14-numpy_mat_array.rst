

.. blogpost::
    :title: Différence entre matrix et array (numpy)
    :keywords: matrix, array
    :date: 2015-06-06
    :categories: calcul matriciel, numpy
    
    Le module `numpy <http://www.numpy.org/>`_ propose
    deux types pour représenter une matrice :
    `array <http://docs.scipy.org/doc/numpy/reference/arrays.html>`_ et 
    `matrix <http://docs.scipy.org/doc/numpy/reference/generated/numpy.matrix.html>`_.
    Le type *matrix* hérite du premier mais se comporte différemment
    dans certaines situations, pour le produit matriciel par exemple.
    Il est parfois utile de vérifier l'objet qu'on manipule
    avant de se perdre en conjecture quant à la source de l'erreur.
    La page
    `Matrix objects <http://docs.scipy.org/doc/numpy/reference/arrays.classes.html#matrix-objects>`_
    est plus explicite à ce sujet.
    
    
    