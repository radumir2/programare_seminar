import unittest  # import biblioteca pentru teste unitare


########################################################################################################################
# DE AICI INCEPE PARTEA DE TESTARE AUTOMATA
class ScriptTests(unittest.TestCase):  # adaug clasa care va contine testele
    def test1(self):                   # cu un prim test "fake" care trece
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
