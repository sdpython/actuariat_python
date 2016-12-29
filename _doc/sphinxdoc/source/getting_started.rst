
.. _l-getting-started-ac:

Installer actuariat_python
==========================

Avec Anaconda sous Windows
++++++++++++++++++++++++++

On s'appuie sur la distribution `Anaconda <https://www.continuum.io/downloads>`_
telle quelle après la première installation.

Le module `actuariat_python <https://pypi.python.org/pypi/actuariat_python>`_ est
disponible sur `pypi <https://pypi.python.org/pypi/actuariat_python>`_.
Il suffit d'utiliser ``pip`` pour l'installer :

::

    pip install actuariat_python

Il affiche alors quelque chose comme :

::

    Successfully installed actuariat-python-0.3.282 autopep8-1.2.4 coverage-4.2 entrypoints-0.2.2
    feedparser-5.2.1 metakernel-0.14.0 mlstatpy-0.1.114 multi-key-dict-2.0.3 pycodestyle-2.0.0
    pyensae-1.1.520 pymyinstall-1.1.1064 pyquickhelper-1.4.1533 pyrsslocal-0.8.197 sphinx-1.4.6
    sphinxcontrib-imagesvg-0.1 sphinxcontrib-jsdemo-0.1.4 sphinxjp.themes.revealjs-0.3.0

Sous Linux (Ubuntu)
+++++++++++++++++++

Selon comment l'installation est faite, il faut utiliser :

::

    pip3 install actuariat_python

ou si une exception ``Permission denied`` survient :

::

    sudo pip3 install actuariat_python

Installer cvxopt
++++++++++++++++

Ce module est difficile à installer car il utilise des librairies qui ne sont
pas souvent présentes par défaut.
Voici ce qu'on peut obtenir sous Windows :

::

    error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\x86_amd64\\cl.exe' failed with exit status 2

Même l'instruction ``conda install cvxopt`` échoue. Dans le cas, il faut soit télécharger le module
depuis `Unofficial Windows Binaries for Python Extension Packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_
ou utiliser :

::

    pymy_install cvxopt

Installer xgboost
+++++++++++++++++

Sous Linux, il suffit de faire (en ajoutant ou non ``sudo``) :

::

    pip3 install xgboost

Sous Windows, il faut soit suivre les instructions décrites sur le site de `XGBoost <https://github.com/dmlc/xgboost/blob/master/doc/build.md>`_
ou dans cet article `Build xgboost on Windows <http://www.xavierdupre.fr/app/pymyinstall/helpsphinx//blog/2016/2016-08-09_xgboost_again.html>`_.
Vous pouvez aussi écrire :

::

    pymy_install xgboost
