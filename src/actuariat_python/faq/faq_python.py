# -*- coding: utf-8 -*-
"""
@file
@brief Quelques questions d'ordre général autour du langage Python.

"""


def instruction_pass():
    """

    Cette fonction ne fait rien.

    .. faqref::
        :title: Quel est l'entier le plus grand ?

        La version 3 du langage Python a supprimé la constante ``sys.maxint``
        qui définissait l'entier le plus grand (voir
        `What's New In Python 3.0
        <https://docs.python.org/3.1/whatsnew/3.0.html#integers>`_).
        De ce fait la fonction `getrandbit
        <https://docs.python.org/3.4/library/random.html#random.getrandbits>`_
        retourne un entier aussi grand que l'on veut.

        .. runpython::
            :showcode:

            import random,sys
            x = random.getrandbits(2048)
            print(type(x),x)

        Les calculs en nombre réels se font toujours avec huit octets de
        précision. Au delà, il faut utiliser la librairie `gmpy2
        <http://gmpy2.readthedocs.org/en/latest/>`_. Il est également
        recommandé d'utiliser cette librairie pour  les grands nombres
        entiers (entre 20 et 40 chiffres). La librairie est plus rapide
        que l'implémentation du langage Python (voir `Overview of gmpy2
        <https://gmpy2.readthedocs.org/en/latest/overview.html>`_).

    .. faqref::
        :title: Tabulations ou espace ?

        Il est préférable de ne pas utiliser les tabulations et de les
        remplacer par des espaces. Lorsqu'on passe d'un Editeur à un autre,
        les espaces ne bougent pas. Les tabulations sont plus ou moins
        grandes visuellement. L'essentiel est de ne pas mélanger.
        Dans `SciTE <http://www.scintilla.org/SciTE.html>`_,
        il faut aller dans le menu Options / Change Indentation Settings...
        Tous les éditeurs ont une option similaire.
    """
    pass
