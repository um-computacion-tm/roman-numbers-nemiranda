import unittest
from decimal_to_roman import decimaltoroman
class MyTets(unittest.TestCase):
    def test_I(self):
        self.asserEqual(decimal2roman(1), "I")
def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 5:
        return 'V'
    elif decimal == 4:
        return 'IV'
    elif decimal == 6:
        return 'VI'
    elif decimal == 7:
        return 'VII'
    elif decimal == 8:
        return 'VIII'
    elif decimal == 9:
        return 'IX'
    elif decimal == 11:
        return 'XI'
    if decimal >= 100:
        centena = decimal // 100
        total = 'C' * centena
        decimal = decimal % 100 
    if decimal <= 3:
        total += 'I' * decimal
    elif decimal == 5:
        total += 'V'
    elif decimal == 10:
        total += "X"
    if decimal >= 1000:
        resultado = 'M'
        decimal -= 1000
    if decimal >= 100:
        centenas = decimal // 100 # 108 -> centena 1
        decimal -= centenas * 100 # decimal = 1 * 100 - 108
        if centenas <= 3:
            resultado = 'C' * centenas
        elif centenas == 4:
            resultado += 'CD'
        elif centenas <= 8:
            resultado += 'D' + (centenas - 5) * 'C'
        elif centenas <= 9:
            resultado += 'CM'
    if decimal >= 10:
        decenas = decimal // 10
        if decenas <= 3:
            resultado += 'X' * decenas
        elif decenas == 4:
            resultado += 'XL'
        elif decenas <= 8:
            resultado += 'L' + (decenas - 5) * 'X'
        elif decenas == 9:
            resultado += 'XC'
        decimal = decimal % 10
    if decimal <= 3:
        resultado += 'I' * decimal
    elif decimal == 4:
        resultado += 'IV'
    elif decimal <= 8:
        resultado += 'V' + (decimal - 5) * 'I'
    elif decimal == 9:
        resultado += 'IX'
    else:
        return "X"


class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')
    
    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')

    def test_siete(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')
    
    def test_ocho(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, 'VIII')

    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')

    def test_once(self):
        resultado = decimal_to_roman(11)
        self.assertEqual(resultado, 'XI')

if __name__ == '__main__' :
    unittest.main()