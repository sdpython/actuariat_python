



.. blogpost::
    :title: Data Wrokflow
    :keywords: orange
    :date: 2015-05-25
    :categories: workflow, data
    :lid: blog-data-workflow
    
    Ce terme désigne une façon plutôt de décrire le traitement de données.
    `Weka <http://www.cs.waikato.ac.nz/ml/weka/>`_ fut un des premiers outils à ouvrir cette voie,
    le premier à devenir une référence. Worflow, dataflow, pipeline sont autant de 
    termes anglais qui désigne un assemblage parfois complexe de traitements 
    appliqués à des données. La représentation la plus naturelle est sous forme 
    de graphe. `Orange <http://orange.biolab.si/>`_ est un outil du même type
    implémenté en Python :

    .. image:: http://orange.biolab.si/static/homepage/screenshots/snp-schema-selection-evaluation.png
        :width: 600

    Ces outils sont assez
    agréables à utiliser lorsque les données se présentent sous des formats classiques, 
    que les données ne nécessitent pas de prétaitement trop complexes. 
    Dès qu'on sort de ces cas, c'est-à-dire souvent, il faut revenir à la programmation.
    Microsoft a récemment lancé sa propre version de ce type d'outil 
    `Azure Machine Learning <https://studio.azureml.net/>`_.