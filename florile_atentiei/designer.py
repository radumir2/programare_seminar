import unittest  # import biblioteca pentru teste unitare
from florile_atentiei.comenzi import Petala


def afiseaza_rezultate(rezultate_studenti):
    comenzi = []
    for al_catelea, rezultate_student in reversed(list(enumerate(rezultate_studenti))):
        if rezultate_student:
            nr_petale = len(rezultate_student)
            for a_cata, rezultat_petala in enumerate(reversed(rezultate_student)):
                comenzi.append(Petala(nr_petale, a_cata+1, al_catelea+1, rezultat_petala))
        else:
            comenzi.append(Petala(1, 1, al_catelea + 1, None))

    return comenzi


class TesteUnitare(unittest.TestCase):
    def test1(self):
        p = Petala(1, 1, 1, None)
        self.assertEqual([str(p)], [str(p) for p in afiseaza_rezultate([[]])])

    def test2(self):
        p1 = Petala(1, 1, 1, None)
        p2 = Petala(1, 1, 2, None)
        p3 = Petala(1, 1, 3, None)
        rezultat_asteptat = [str(p3), str(p2), str(p1)]
        rezultat_obtinut = [str(p) for p in afiseaza_rezultate([[], [], []])]
        self.assertEqual(rezultat_asteptat, rezultat_obtinut)

    def test3(self):
        p1 = Petala(1, 1, 1, True)
        p2 = Petala(1, 1, 2, None)
        p3 = Petala(1, 1, 3, None)
        rezultat_asteptat = [str(p3), str(p2), str(p1)]
        rezultat_obtinut = [str(p) for p in afiseaza_rezultate([[True], [], []])]
        self.assertEqual(rezultat_asteptat, rezultat_obtinut)


if __name__ == "__main__":
    unittest.main()
