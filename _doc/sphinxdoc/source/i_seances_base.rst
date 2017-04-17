
.. _l-seances-base:

======================================
Exercices de programmation avec Python
======================================

Ces séances reprennent les contenus proposés sur plusieurs années.
La plupart des outils qui traitent des données, même s'ils
paraissent simples d'usage, proposent toujours des portes dérobées
pour insérer un programme écrit en Python, en R ou autre langage.
Il est très rare de pouvoir tout faire d'un clic de souris.

.. contents::
    :local:
    :maxdepth: 1

Découvertes
===========

.. toctree::
    :maxdepth: 2

    notebooks/pandas_start
    notebooks/table_avec_guillemets

*Lectures*

* `Machine Learning, Statistiques et Programmation <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/index.html#jupytalk>`_
  (voir aussi `Présentations en notebooks <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/index.html>`_)
* `Initiation à la programmation et l'algorithmie <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_1a.html>`_ (ENSAE)
* `Python pour un Data Scientist <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_2a.html>`_ (ENSAE)
* :ref:`Data workflow <blog-data-workflow>`

Simulation de population
========================

Une population est décrite par de nombreux critères, âge, genre, nombre, revenus...
Et la plupart du temps, on souhaite regarde comment elle évolue à partir de certaines
hypothèses. Ces exercices proposent quelques exemples sur ce sujet.

.. toctree::
    :maxdepth: 2

    notebooks/_gs4_simulation_population

Gros volumes de données
=======================

Les grandes bases de données sont agaçantes. Elles ne tiennent
pas en mémoire et tout prend plus de temps. Cette partie présente quelques
astuces pour être plus efficace.

.. toctree::
    :maxdepth: 2

    notebooks/_gs5_sql_big_data
    notebooks/_gs5_cube
    notebooks/_gs5_approche_fonctionnelle
    notebooks/_gs_internet

*Lectures*

* `A thorough guide to SQLite database operations in Python <http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html>`_
* `Eléments logiciels pour le traitement des données massives <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/td_3a.html>`_ (ENSAE)

Graphes
=======

Une partie essentielle et parfois rébarbative lorsqu'il s'agit de
tracer une carte. Ces notebooks sont une bonne source pour du copier coller.

.. toctree::
    :maxdepth: 2

    notebooks/_gs6_graphe
    notebooks/_gs6_graphe_ml

*Lectures*

* :ref:`blog-2016-06-14-plotting`
* `10 plotting libraries <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2016/pydata2016.html>`_

Etre inventif et fabriquer ce qu'on n'a pas
===========================================

Comment découper un problème compliqué en problèmes plus simples ?

.. toctree::
    :maxdepth: 2

    notebooks/_gs7_synonyme
    notebooks/_gs_gerrymandering

*Lectures*

* `Work on the features or the model <http://www.xavierdupre.fr/blog/2015-03-07_nojs.html>`_
* `Un BOT à partir d'un assemblage d'IA <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2017/devoxx2017.html>`_
