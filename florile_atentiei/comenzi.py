import unittest


class Petala():
    def __init__(self, nr_total, nr_petala, nr_student, rezultat):
        self.nr_total = nr_total
        self.nr_petala = nr_petala
        self.nr_student = nr_student
        self.rezultat = rezultat

    def __str__(self):
        return f"{self.nr_petala}:{self.nr_total} pt {self.nr_student} cu {self.rezultat}"

    __repr__ = __str__


class TesteUnitare(unittest.TestCase):
    def test1(self):
        p = Petala(10, 2, 1, True)
        self.assertEqual("2:10 pt 1 cu True", str(p))

    def test2(self):
        p1 = Petala(3, 1, 1, False)
        p2 = Petala(3, 1, 1, False)
        self.assertEqual(str(p1), str(p2))


if __name__ == "__main__":
    unittest.main()
