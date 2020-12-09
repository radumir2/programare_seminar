import unittest
import json
from collections import OrderedDict


class Optiune:
    def __init__(self, text, buna):
        self.text = text
        self.e_buna = buna

    def as_json(self):
        odict = OrderedDict()
        odict["text"] = self.text
        odict["buna"] = self.e_buna
        return json.dumps(odict)


class Exercitiu:
    def __init__(self, nume, context, enunt, optiuni):
        self.nume = nume
        self.context = context
        self.enunt = enunt
        self.optiuni = optiuni

    def optiuni_ca_string(self):
        optiuni_s = [o.as_json() for o in self.optiuni]
        return f"[{', '.join(optiuni_s)}]"

    def as_json(self):
        odict = OrderedDict()
        odict["nume"] = self.nume
        odict["context"] = self.context
        odict["enunt"] = self.enunt
        odict["optiuni"] = "__OPTIUNI__"
        result = json.dumps(odict)
        result = result.replace("\"__OPTIUNI__\"", self.optiuni_ca_string())
        return result

class TestUnitare(unittest.TestCase):
    def test01_json(self):
        self.assertEqual("{\"a\": 1}", json.dumps({"a": 1}))

    def test02_optiune(self):
        opt = Optiune("True", True)
        self.assertEqual("{\"text\":\"True\", \"buna\":true}", json.dumps(opt))


if __name__ == "__main__":
    unittest.main()
