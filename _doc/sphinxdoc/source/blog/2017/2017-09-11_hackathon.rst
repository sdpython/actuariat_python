
.. blogpost::
    :title: Hackathon - Institut des Actuaires
    :keywords: python, machine learning
    :date: 2017-09-11
    :categories: hackathon

    `Crésus <http://www.cresus-iledefrance.org/>`_ accompagne les personnes en situation de
    surendettement. Les personnes en situation financière difficile commencent par envoyer
    un dossier qui précisent les éléments principaux de leur situation. C'est ce que contiennent les bases
    *dossier*, *budget*. Un ou plusieurs rendez-vous téléphonique suit pour renseigné les
    tables *agenda* et *crédit*.
    Deux colonnes sont utilisées pour qualifier la nature de la situation (diagnostic)
    et l'orientation donnée au dossier. Ce sont les deux informations qu'il faut prédire.
    Pour ce faire, les tables sont été divisés en apprentissage et test
    selon deux ensembles disjoints dans le temps de dossiers.
    La base de dossier ne contient pas d'historique.
    C'est une vue de la situation au moment où le dossier est orienté.

    **Mode d'emploi**

    Les différents fichiers sont un dump des différentes tables du système
    d'information de l'association. Elles sont liées par des identifiants.
    L'identifiant dossier est celui qui permet de lier les données
    de la table principale *dossier* aux autres.
    La table *dossier* est scindée en deux parties :

    * *X* : ensemble des colonnes saisies à la réception d'un dossier
    * *Y* : ensemble des informations renseignées manuellement après l'étude d'un dossier.

    La partie *Y* contient deux colonnes :

    * *nature* : un diagnostique, une raison qui explique le surendettement

    Il faut prédire cette colonne.
    **Il ne faut pas utiliser les colonne etat et nature** qui sont renseignées
    manuellement après *orientation*.

    **Compétition**

    La compétition est accessible sur codalab :
    `Hackathon Institut des Actuaires <https://competitions.codalab.org/competitions/17411>`_.
    C'est un problème de classification **multi-classes**.

    * `données du challenge <https://github.com/sdpython/actuariat_python/blob/master/_doc/competitions/2017_IA_hackathon/competition/data_cresus.zip>`_

    Les réponses doivent être données dans le même ordre que les lignes de la table
    ``tbl_dossier.test.X.txt`` dans un fichier texte sans en-tête **answer.txt**.
    Soumettre une solution consiste à envoyer à fichier **answer.zip** qui contient un
    fichier **answer.txt** au format suivant :

    ::

        4.0  0.9144635693307518
        2.0  0.9058230082126213
        1.0  0.963522847810654
        2.0  0.6700924948192609
        5.0  0.33637962518435127
        1.0  0.2746943724528652
        5.0  0.695436159178639

    Avec deux colonnes :

    #. prédiction pour l'**orientation**
    #. **score orientation** pour la prédiction de l'orientation

    Un exemple de soumission est disponible (réponse aléatoire)

    #. `answer.txt <https://github.com/sdpython/actuariat_python/blob/master/_doc/competitions/2017_IA_hackathon/competition/answer.txt>`_
    #. `answer.zip <https://github.com/sdpython/actuariat_python/blob/master/_doc/competitions/2017_IA_hackathon/competition/answer.zip>`_

    Les métriques produites pour chaque colonne :

    * **ERR - taux d'erreur** : c'est la proportion de mauvaises prédictions,
      la classe prédite n'est pas la classe attendue.
    * **AUC - aire sous la courbe ROC** : ce chiffre correspond à la probabilité
      pour le score d'une bonne prédiction d'être supérieur au score d'une mauvaise
      prédiction - `Courbe ROC <http://www.xavierdupre.fr/app/mlstatpy/helpsphinx/c_metric/roc.html>`_.

    Une bonne *AUC* indique que le score de la prédiction est fiable.
    Autrement dit, même si le taux d'erreur est élevé, cela signifie que celui qui utilise
    le modèle de prédiction peut plus facilement croire la prédiction quand celle-ci est élevée.
    Cette métrique a été choisie pour permettre à l'utilisateur d'automatiser
    une partie du traitement avec fiabilité et de continuer à gérer les autres
    dossiers manuellement lorsque la prédiction n'est pas assez fiable.
    La fonction de calcul *AUC*
    est implémentée : :func:`AUC_multi <ensae_projects.ml.competitions.AUC_multi>`
    et le fichier d'évaluation fonctionne en Python 2 ou 3 :
    `evaluate.py <https://github.com/sdpython/actuariat_python/blob/master/_doc/competitions/2017_IA_hackathon/competition/program/evaluate.py>`_.

    **Autres données**

    * `dataforgoodfr/croixrouge <https://github.com/dataforgoodfr/croixrouge/tree/master/data>`_
    * `Description des tables INSEE <https://github.com/dataforgoodfr/croixrouge/wiki/Description-des-tables-INSEE>`_
    * `data.gouv.fr <https://www.data.gouv.fr/fr/>`_
