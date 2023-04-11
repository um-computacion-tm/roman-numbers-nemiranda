import unittest

def roman_to_decimal(roman):
    return 1

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')

        self.assertEqual(resultado, 1)
        
    def test_II(self):
        resultado = roman_to_decimal('II')

        self.assertEqual(resultado, 2)
        
    def test_III(self):
        resultado = roman_to_decimal('III')

        self.assertEqual(resultado, 3)
        
    def test_IV(self):
        resultado = roman_to_decimal('IV')

        self.assertEqual(resultado, 4)
        
    def test_V(self):
        resultado = roman_to_decimal('V')

        self.assertEqual(resultado, 5)
        
    def test_VI(self):
        resultado = roman_to_decimal('VI')

        self.assertEqual(resultado, 6)
       

if __name__ == '__main__':
    unittest.main()
