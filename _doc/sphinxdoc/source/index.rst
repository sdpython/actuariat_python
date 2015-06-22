
Python et actuariat
===================

   
   
**Links:** `pypi <https://pypi.python.org/pypi/actuariat_python/>`_, 
`github <https://github.com/sdpython/actuariat_python/>`_,
`documentation <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html>`_,
`wheel <http://www.xavierdupre.fr/site2013/index_code.html#actuariat_python>`_,
`travis <https://travis-ci.org/sdpython/actuariat_python>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`


en développement


Contenu
-------

.. toctree::
    :maxdepth: 1

    seances_2015


.. _l-getting-started-main:
.. _l-install:


Liens, articles
---------------

* `ENSAE 1A : Initiation à la programmation et l'algorithmie <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_1a.html>`_
* `ENSAE 2A : Données, Machine Learning et Programmation <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a.html>`_
* `ENSAE 3A : Eléments logiciels pour le traitement des données massives <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_3a.html>`_
* `Python pour un datascientist <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/data2a.html>`_
* :ref:`Data workflow <blog-data-workflow>`
* :ref:`Work on the features or the model <http://www.xavierdupre.fr/blog/2015-03-07_nojs.html>`_


Getting started
---------------


La page 
`Getting started (ENSAE) <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html#getting-started>`_
décrit les instructions pour installer Python et tous les modules
nécessaires pour exécuter les notebooks. Sous Windows, l'option recommandée est 
`WinPython <https://winpython.github.io/>`_. Open source, cette distribution peut être personnalisée
avec des modules propres à une entreprise.

Une fois l'installation terminée, il est préférable de faire quelques tests
pour vérifier que tout s'est bien passé. On peut par exemple
exemple exécuter le notebook :ref:`populationrecuperationdonneesrst`.

**Recommandations**

* Linux/Mac OS : distribution `Anaconda <http://continuum.io/downloads#py34>`_ (python 3.4, 64 bit)
* Windows : distribution `WinPython <https://winpython.github.io/>`_

**Installer un module**

Il faut ouvrir une fenêtre ligne de commande (Windows) ou une fenêtre terminal (Linux, OS/X) et se placer dans le répertoire de la distribution.

* Anaconda: 

    * module standard : ``conda install <module>``
    * module rare : ``pip install <module>``
    
* WinPython

    * module standard : télécharger le module sur le site `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ 
      et l'installer avec la commande ``pip install <local_module.whl>``
    * module rare : ``pip install <module>`` (à condition que celui-ci n'inclut pas de code C/C++) qui requiert un compilateur C/C++
    
**Problème de dépendance**

Pour installer rapidement un module sans tenir compte de ses dépendances ::

    pip install <module> --no-deps
    
**Mettre à jour un module**

::

    pip install <module> --upgrade --no-deps
    
L'extension *--no-deps* n'est pas obligatoire mais cela évite la mise à jour des dépendances.


    

Table des matières
------------------

.. toctree::
    :maxdepth: 1

    blog/main_0000
    all_notebooks
    all_example
    README
    glossary
    azFAQ
    license
    filechanges
    

Index
-----

* :ref:`l-notebooks`
* :ref:`modindex` (résumé :ref:`l-modules`)
* :ref:`l-classes`
* :ref:`l-functions`
* `Unit Test Coverage <coverage/index.html>`_
* :ref:`search`

.. image:: https://travis-ci.org/sdpython/actuariat_python.svg?branch=master
    :target: https://travis-ci.org/sdpython/actuariat_python
    :alt: Build status
    
.. image:: https://badge.fury.io/py/actuariat_python.svg
    :target: http://badge.fury.io/py/actuariat_python
      
.. image:: http://img.shields.io/pypi/dm/actuariat_python.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/actuariat_python

.. image:: http://img.shields.io/github/issues/sdpython/actuariat_python.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/actuariat_python/issues
    
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT
