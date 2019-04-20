# -*- coding: utf-8 -*-
"""
@brief      test log(time=60s)
"""
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestExam2016(unittest.TestCase):

    def setUp(self):
        # add_missing_development_version(
        #    ["pyensae", "pymyinstall", "pyrsslocal"], __file__)
        pass

    def test_data_2016(self):
        """
        Questions

        1. Deux fichiers sont extraits de la base de données d'un médecin.
           Un fichier contient des informations sur des personnes, un autre
           sur les rendez-vous pris par ces personnes. Quels sont-ils ?

        2. On souhaite étudier la relation entre le prix moyen payés par une personne,
           son âge et son genre. Calculer le prix moyen payé par une personne ?

        3. Faire la jointure entre les deux tables.

        4. Tracer deux nuages de points (age, prix moyen) et (genre, prix moyen) ?

        5. Calculer les coefficients de la régression prix moyen ~ age + genre.

        6. On souhaite étudier le prix d'une consultation en fonction du jour de la semaine.
           Ajouter une colonne dans la table de votre choix avec le jour de la semaine.

        7. Créer un graphe moustache qui permet de vérifier cette hypothèse.

        8. Ajouter une colonne dans la table de votre choix qui contient
           365 si c'est le premier randez-vous, le nombre de jour écoulés
           depuis le précédent rendez-vous. On appelle cette colonne delay.
           On ajoute également la colonne 1/delay.

        9. Calculer les coefficients de la régression
           prix ~ age + genre + delay + 1/delay + jour_semaine.

        10. Comment comparer ce modèle avec le précédent ?
            Implémentez le calcul qui vous permet de répondre à cette question.
        """
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from actuariat_python.exams.ex2016 import enumerate_person, enumerate_appointments
        f = list(enumerate_person(n=1))
        assert isinstance(f[0], dict)
        df = pandas.DataFrame(enumerate_person(n=1000))
        self.assertEqual(df.shape, (1000, 4))
        fLOG(df.head())

        persons = df.to_dict("records")
        ap = pandas.DataFrame(enumerate_appointments(persons))
        fLOG(ap.head())

        temp = get_temp_folder(__file__, "temp_data_2016")
        f1 = os.path.join(temp, "persons.txt")
        df.to_csv(f1, index=False, sep="\t")
        f2 = os.path.join(temp, "rendezvous.txt")
        ap.to_csv(f2, index=False, sep="\t")

        assert os.path.exists(f1)
        assert os.path.exists(f2)


if __name__ == "__main__":
    unittest.main()
