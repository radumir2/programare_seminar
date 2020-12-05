import unittest  # import biblioteca pentru teste unitare
import os

# Problema Pinochio
# Lui Pinochio ii creste nasul cu rata_crestere in fiecare zi lucratoare.
# In weekend, cand e cu Gepeto, nu minte si nasul ii scade cu 1 cm.
# Stiind lungimea_initiala_nas a nasului, rata_crestere sa se afle
# lungimea nasului dupa numar_de_zile


def lungime_nas_pinochio_f(lungime_initiala_nas, rata_crestere, numar_de_zile):
    def pinochio_cu_acumulator(acumulator, rata_crestere, numar_de_zile, zi):
        if numar_de_zile == 0:
            return acumulator

        zi_saptamana = zi % 7
        if zi_saptamana % 7 == 0:
            zi_saptamana = 7

        if zi_saptamana < 6:  # nu sunt in weekend
            return pinochio_cu_acumulator(acumulator + rata_crestere, numar_de_zile - 1, zi + 1)
        else:
            return pinochio_cu_acumulator(acumulator - 1, numar_de_zile - 1, zi + 1)

    return pinochio_cu_acumulator(lungime_initiala_nas, rata_crestere, numar_de_zile, 1)


def lungime_nas_pinochio(lungime_initiala_nas, rata_crestere, numar_de_zile):
    rezultat = lungime_initiala_nas

    for zi in range(numar_de_zile):
        zi_saptamana = (zi + 1) % 7
        if zi_saptamana == 0:
            zi_saptamana = 7

        if zi_saptamana < 6:  # nu e weekend
            rezultat = rezultat + rata_crestere
        else:  # e in weekend
            rezultat = rezultat - 1

    return rezultat  # lungimea nasului lui Pinochio la sfarsit


########################################################################################################################
# DE AICI INCEPE PARTEA DE TESTARE AUTOMATA
class ScriptTests(unittest.TestCase):  # adaug clasa care va contine testele
    def _test_generic(self, nume_test):
        # obtin continutul fisierului
        cale_fisier = f"{os.path.dirname(os.path.realpath(__file__))}/{nume_test}.txt"
        with open(cale_fisier, "r") as f:
            file_content = f.read()

        # ... si il spart in parti
        parti_fisier = file_content.split("=====")

        # ... din care iau date intrare
        date_intrare = parti_fisier[0].strip()
        # ... si rezultat (care trebuie sa fie un int)
        rezultat_asteptat = int(parti_fisier[1].strip())

        # separ datele de intrare cu spatiu si obtin parametrii de apel
        lista_date_intrare = date_intrare.split(" ")
        lungime_initiala_nas = int(lista_date_intrare[0])
        rata_crestere_nas = int(lista_date_intrare[1])
        perioada = int(lista_date_intrare[2])

        # apelez functia principala si obtin rezultatul real
        rezultat_real = lungime_nas_pinochio(lungime_initiala_nas, rata_crestere_nas, perioada)

        # ... pe care-l compar cu rezultatul asteptat
        self.assertEqual(rezultat_asteptat, rezultat_real)

    def test1(self):
        self._test_generic("test1")

    def test2(self):
        self._test_generic("test2")

    def test3(self):
        self._test_generic("test3")


if __name__ == "__main__":
    unittest.main()
