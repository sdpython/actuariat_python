

.. blogpost::
    :title: Jupyter et R
    :keywords: kernel
    :date: 2016-04-07
    :categories: Jupyter, R
    
    `Jupyter <http://jupyter.org/>`_ fonctionne aussi avec 
    `R <https://www.r-project.org/>`_ 
    (voir `Supports de cours en R <http://freakonometrics.hypotheses.org/48364>`_).
    L'installation repose sur les éléments suivants :
    
    * Installer Jupyter (avec `Anaconda <https://www.continuum.io/downloads>`_) par exemple)
    * Mettre à jour la distribution (``conda update --all``)
    * Installer `R <https://www.r-project.org/>`_ 
    * Installer le package `IRKernel <https://github.com/IRkernel/IRkernel>`_ en suivant
      les instructions décrites sur le site de IRKernel
    * Installer le *kernel* toujours en suivant les instructions du site IRKernel
    
    Cette dernière étape devrait installer un fichier *json* 
    (dans ``C:\ProgramData\jupyter\kernels`` sous Windows) qui
    ressemble à : 
    
    ::
    
        {"display_name": "R", 
         "argv": ["C:\\Program Files\\R\\bin\\x64\\R.exe", 
                  "--quiet", "-e", "IRkernel::main()", 
                  "--args",  "{connection_file}"], 
         "language": "R"}
    
    On peut trouver des *kernels* pour les autres langages
    `IPython kernels for other languages <https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages>`_.
    Le *kernel* est le bout de code qui gère la communication entre Jupyter et l'interpréteur ou le compilateur 
    du langage considéré.
    