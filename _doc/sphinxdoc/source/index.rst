Python pour un Actuaire
=======================

   
   
**Links:** `pypi <https://pypi.python.org/pypi/actuariat_python/>`_, 
`github <https://github.com/sdpython/actuariat_python/>`_,
`documentation <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html>`_,
`wheel <http://www.xavierdupre.fr/site2013/index_code.html#actuariat_python>`_


Quelques digressions actuarielles.


Contenu
-------

en construction

.. toctree::

    seances


.. _l-getting-started-main:
.. _l-install:


Getting started
---------------

.. index:: R, Julia, WinPython, Anaconda, pyminstall


La version recommandée est Python 3.4, 64 bit. Par défaut, les modules 
s'installe avec ``pip install <module>``. Deux distrubutions possibles :

* `Anaconda <http://continuum.io/downloads#py34>`_ (Windows, Linux, Mac). 
  Sous Linux ou Mac, la distribution n'interfère pas avec la distribution existante
  souvent différente. C'est un point très appréciable. Les modules de la distribution ne sont 
  pas tous à jour. Il faut penser à mettre à jour avec la commande ``conda install <module>``
  depuis le répertoire ``Anaconda3/Scripts`` (``conda install pandas`` par exemple).
  Pour suivre ces cours il faut ajouter :

    * `cvxopt <http://cvxopt.org/>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/#cvxopt>`_)
    * `goslate <http://pythonhosted.org/goslate/>`_
    * `dbfread <http://dbfread.readthedocs.org/en/latest/>`_
    * `rpy2 <http://rpy.sourceforge.net/>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/#rpy2>`_)
    * `mpld3 <http://mpld3.github.io/>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_)
    * `folium <https://github.com/python-visualization/folium>`_
    * `graphviz <https://github.com/xflr6/graphviz>`_
    * `numexpr <https://github.com/pydata/numexpr>`_
    
   Il existe une version différente : `miniconda <http://conda.pydata.org/miniconda.html>`_.
   La liste des packages manquant sera probablement différente.

* `WinPython <https://winpython.github.io/>`_ (Windows). Sous Windows, elle a l'avantage d'inclure
  `R <http://www.r-project.org/>`_ ou `Julia <http://julialang.org/>`_. On passe alors
  facilement de python à R ou Julia depuis le même notebooks. Pour suivre ces cours il faut ajouter :

    * `goslate <http://pythonhosted.org/goslate/>`_
    * `dbfread <http://dbfread.readthedocs.org/en/latest/>`_
    * `bokeh <http://bokeh.pydata.org/en/latest/>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/#bokeh>`_)
    * `pywin32 <https://pypi.python.org/pypi/pywin32>`_ (`Windows <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32>`_)
    * `folium <https://github.com/python-visualization/folium>`_
    * `graphviz <https://github.com/xflr6/graphviz>`_    
    
Sous Linux, l'installation ne pose pas de problèmes. Sous Windows, il faut installer
les packages `wheel <http://wheel.readthedocs.org/en/latest/>`_. Ces modules
sont accessibles depuis le site `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
Vous pouvez également utiliser le module `pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
et écrire ::

    from pymyinstall import extend_anaconda, process_installation
    process_installation(extend_anaconda())

Ou ::
    
    from pymyinstall import extend_winpython, process_installation
    process_installation(extend_winpython())
    
Enfin, il est possible d'utiliser la distribution standard de Python. La liste des modules
nécessaire est assez longue et peut-être trouvée dans le code de la fonction
`complete_installation <https://github.com/sdpython/pymyinstall/blob/master/src/pymyinstall/packaged/packaged_config.py>`_
que vous pouvez exécuter après avoir installé le module 
`pymyinstall <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html>`_
avec le code suivant ::    

        from pymyinstall import datascientist
        datascientist("install", full = True)
        
Certains notebooks requièrent des outils supplémentaires :

    * `graphviz <http://www.graphviz.org/>`_
    
    

Table des matières
------------------

.. toctree::
    :maxdepth: 1

    all_notebooks
    all_example
    README
    glossary
    FAQ
    license
    filechanges

Index
-----

* :ref:`l-notebooks`
* :ref:`l-modules`
* :ref:`l-classes`
* :ref:`l-functions`
* `Unit Test Coverage <coverage/index.html>`_
* :ref:`search`




