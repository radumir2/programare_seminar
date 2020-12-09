import unittest
import json
from collections import OrderedDict


class Optiune:
    def __init__(self, text, buna):
        self.text = text
        self.e_buna = buna

    def as_json_object(self):
        odict = OrderedDict()
        odict["text"] = self.text
        odict["buna"] = self.e_buna
        return odict


class ExercitiuBuilder:
    def __init__(self, name):
        self.nume = name
        self.context = []
        self.enunt_ex = None
        self.optiuni = []

    def enunt(self, enunt):
        self.enunt_ex = enunt

    def optiune(self, line):
        buna = False
        if line.startswith("+ "):
            line = line[2:]
            buna = True
        o = Optiune(line, buna)
        self.optiuni.append(o)

    def end(self):
        return Exercitiu(self.nume, self.context, self.enunt_ex, self.optiuni)


class Exercitiu:
    def __init__(self, nume, context, enunt, optiuni):
        self.nume = nume
        self.context = context
        self.enunt = enunt
        self.optiuni = optiuni

    def as_json(self):
        odict = OrderedDict()
        odict["nume"] = self.nume
        odict["context"] = self.context
        odict["enunt"] = self.enunt
        odict["optiuni"] = [o.as_json_object() for o in self.optiuni]
        return json.dumps(odict)


class TestUnitare(unittest.TestCase):
    def test01_json(self):
        self.assertEqual("{\"a\": 1}", json.dumps({"a": 1}))

    def test02_optiune(self):
        opt = Optiune("True", True)
        self.assertEqual("{\"text\": \"True\", \"buna\": true}", json.dumps(opt.as_json_object()))

    def test_parsat_ex(self):
        text = """:ex range(N)
:enunt range(10)
:optiune + range(0, 10)
:optiune [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
:optiune [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
:end
"""
        linii = text.split("\n")
        builder = None
        exercitiu = None
        for linie in linii:
            if linie == ":end":
                exercitiu = builder.end()
            elif linie.startswith(":"):
                comanda, argument = linie.split(" ", 1)
                if comanda == ":ex":
                    builder = ExercitiuBuilder(argument)
                elif comanda == ":enunt":
                    builder.enunt(argument)
                elif comanda == ":optiune":
                    builder.optiune(argument)
        self.assertEqual("{\"nume\": \"range(N)\", \"context\": [], \"enunt\": \"range(10)\", " + \
                         "\"optiuni\": [{\"text\": \"range(0, 10)\", \"buna\": true}, " +
                         "{\"text\": \"[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\", \"buna\": false}, "+
                         "{\"text\": \"[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\", \"buna\": false}]}",
                         exercitiu.as_json())


if __name__ == "__main__":
    unittest.main()
