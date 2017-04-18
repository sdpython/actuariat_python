
.. blogpost::
    :title: Mettre à jour un module sous Windows
    :keywords: update, pip, Windows
    :date: 2016-11-15
    :categories: module
    :lid: blog-installer-module

    Comme il n'existe pas de compilateur par défaut sous Windows,
    l'installation ou la mise à jour des modules requiert de
    passer toujours par les mêmes étapes.
    Si la distribution `Anaconda <https://www.continuum.io/downloads>`_
    est installée et que le module est maintenu, il faut toujours exécuter :

    ::

        conda install <module>

    Et :

    ::

        conda update <module>

    Si le module n'est pas maintenu ou que la distribution
    `Anaconda <https://www.continuum.io/downloads>`_  n'est pas utilisé,
    il existe trois cas possibles.

    #. Le module est écrit en Python pur (exemple : `seaborn <http://seaborn.pydata.org/>`_).
    #. Le module contient du C++ et est compilé par le site
       `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
       (exemple : `numpy <http://www.numpy.org/>`_).
    #. Le module contient du C++ et n'est pas compilé par le site
       `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ :
       (exemple : `xgboost <https://github.com/dmlc/xgboost>`_).

    Le **cas 1** est simple si le module dépend de modules tous
    écrits en Python (voir plus bas). Il suffit d'exécuter :

    ::

        pip install <module>

    Ou :

    ::

        pip install <module> --upgrade

    Si on souhaite installer ou mettre à jour le module sans les
    dépendances, il faut ajouter l'option ``--no-deps``. Cette option
    est indispensable lorsqu'on met à jour un module qui prend une dépendance
    sur un autre module qui contient du C++ comme
    `seaborn <http://seaborn.pydata.org/>`_.
    La mise à jour de ce module entraîne la mise à jour de
    `numpy <http://www.numpy.org/>`_ qui échoue car elle requiert
    un compilateur C++ et `Intel® Math Kernel Library <https://software.intel.com/en-us/intel-mkl>`_.

        NumPy, a fundamental package needed for scientific computing with Python.
        Numpy+MKL is linked to the Intel® Math Kernel Library and includes required DLLs in the numpy.core directory.

    Le **cas 2** est simple aussi dans la mesure où il suffit de télécharger le fichier
    *.whl* depuis le site `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
    Une fois ce fichier téléchargé, il suffit d'exécuter :

    ::

        pip install <fichier>

    La mise à jour se fait de la même façon :

    ::

        pip install <fichier>

    Le **cas 3** est plus complexe. Il requiert que le module
    soit compilé. `Pypi <https://pypi.python.org/pypi>`_ propose parfois une version
    compilée comme pour `scipy <https://pypi.python.org/pypi/scipy>`_
    mais il faut vérifier qu'il existe une version pour la distribution
    de Python installée. Il existe deux sous-cas.

    **Cas 3.1 :** le site du module explique comment compiler
    le module sous Windows. C'est le cas de xgboost.
    Lire `Build xgboost on Windows <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2016/2016-08-09_xgboost_again.html>`_.

    **Cas 3.2 :** le module peut être compilé avec les instructions
    standard.
    Exemple : `Build param on Windows <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2016/2016-08-16_param.html>`_.

    **Que fait le module pymyinstall ?**

    Le module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//index.html>`_
    peut installer ou mettre à jour une
    `liste de modules <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx///ensae_full_set_table.html?highlight=list>`_
    utilisée pour mes enseignements. C'est un mélange de module Python (cas 1), de module C++
    accessibles depuis le site
    `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
    ou non (cas 3). Dans ce dernier cas, le module va chercher la dernière version
    compilé sur le site *www.xavierdupre.fr*.
    Pour s'en servir :

    ::

        pymy_install <module>

    Ou pour mettre à jour :

    ::

        pymy_update <module>

    Les instructions pour compiler certains modules compliqués sont
    décrites sur ce `blog <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx////blog/main_0000.html>`_.
