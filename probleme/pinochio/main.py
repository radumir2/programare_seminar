import unittest  # import biblioteca pentru teste unitare
import os


def lungime_nas_pinochio(lungime_initiala_nas, rata_crestere, numar_de_zile):
    return 0  # lungimea nasului lui Pinochio la sfarsit


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


if __name__ == "__main__":
    unittest.main()
