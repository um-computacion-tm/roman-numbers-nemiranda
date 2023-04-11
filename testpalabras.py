import unittest
from contadorpalabras import contadordepalabras
class TestContarPalabras(unittest.TestCase):

    def test_simple(self):
        result = contadordepalabras('hola')
        self.assertEqual(result, {'hola': 1})