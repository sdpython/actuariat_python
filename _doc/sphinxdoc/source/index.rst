
Python pour un actuaire
=======================

   
   
**Links:** `pypi <https://pypi.python.org/pypi/actuariat_python/>`_, 
`github <https://github.com/sdpython/actuariat_python/>`_,
`documentation <http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html>`_,
`wheel <http://www.xavierdupre.fr/site2013/index_code.html#actuariat_python>`_,
`travis <https://travis-ci.org/sdpython/actuariat_python>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`


Quelques digressions actuarielles.


Contenu
-------

.. toctree::
    :maxdepth: 1

    seances_2015


.. _l-getting-started-main:
.. _l-install:


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

Data workflow
-------------

Ce terme désigne une façon plutôt de décrire le traitement de données.
`Weka <http://www.cs.waikato.ac.nz/ml/weka/>`_ fut un des premiers outils à ouvrir cette voie,
le premier à devenir une référence. Worflow, dataflow, pipeline sont autant de 
termes anglais qui désigne un assemblage parfois complexe de traitements 
appliqués à des données. La représentation la plus naturelle est sous forme 
de graphe. `Orange <http://orange.biolab.si/>`_ est un outil du même type
implémenté en Python :

.. image:: http://orange.biolab.si/static/homepage/screenshots/snp-schema-selection-evaluation.png

Ces outils sont assez
agréables à utiliser lorsque les données se présentent sous des formats classiques, 
que les données ne nécessitent pas de prétaitement trop complexes. 
Dès qu'on sort de ces cas, c'est-à-dire souvent, il faut revenir à la programmation.
Microsoft a récemment lancé sa propre version de ce type d'outil 
`Azure Machine Learning <https://studio.azureml.net/>`_.
    

Table des matières
------------------

.. toctree::
    :maxdepth: 1

    blog/blogindex
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
