import unittest

from calculadora import Calculadora


class TestCalcu(unittest.TestCase):
    
    def test_sumar(self):
        calc = Calculadora()
        self.assertEqual(calc.sumar(1, 1), 2)

    def test_sumar_negativos(self):
        calc = Calculadora()
        self.assertEqual(calc.sumar(-1, -1), -2)

    def test_sumar_con_cero(self):
        calc = Calculadora()
        self.assertEqual(calc.sumar(0, -1), -1)


if __name__ == "__main__":
    unittest.main()
