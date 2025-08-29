import unittest

from calculadora import Calculadora  # suponiendo que está en calculadora.py


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    # --- Sumar ---
    def test_sumar_positivos(self):
        self.assertEqual(self.calc.sumar(3, 5), 8)

    def test_sumar_negativos(self):
        self.assertEqual(self.calc.sumar(-3, -5), -8)

    def test_sumar_mixto(self):
        self.assertEqual(self.calc.sumar(-3, 5), 2)

    def test_sumar_con_cero(self):
        self.assertEqual(self.calc.sumar(0, 7), 7)

    # --- Restar ---
    def test_restar_positivos(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_restar_negativos(self):
        self.assertEqual(self.calc.restar(-10, -4), -6)

    def test_restar_mixto(self):
        self.assertEqual(self.calc.restar(-3, 5), -8)

    def test_restar_con_cero(self):
        self.assertEqual(self.calc.restar(7, 0), 7)

    # --- Multiplicar ---
    def test_multiplicar_positivos(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_multiplicar_negativos(self):
        self.assertEqual(self.calc.multiplicar(-3, -4), 12)

    def test_multiplicar_mixto(self):
        self.assertEqual(self.calc.multiplicar(-3, 4), -12)

    def test_multiplicar_por_cero(self):
        self.assertEqual(self.calc.multiplicar(7, 0), 0)

    # --- Dividir ---
    def test_dividir_positivos(self):
        self.assertEqual(self.calc.dividir(8, 2), 4)

    def test_dividir_negativos(self):
        self.assertEqual(self.calc.dividir(-8, -2), 4)

    def test_dividir_mixto(self):
        self.assertEqual(self.calc.dividir(-8, 2), -4)

    def test_dividir_con_cero_numerador(self):
        self.assertEqual(self.calc.dividir(0, 5), 0)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(5, 0)

    # --- Potencia ---
    def test_potencia_positiva(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)

    def test_potencia_cero_exponente(self):
        self.assertEqual(self.calc.potencia(5, 0), 1)

    def test_potencia_exponente_negativo(self):
        self.assertAlmostEqual(self.calc.potencia(2, -2), 0.25)

    def test_potencia_base_negativa(self):
        self.assertEqual(self.calc.potencia(-2, 3), -8)

    def test_potencia_base_cero(self):
        self.assertEqual(self.calc.potencia(0, 3), 0)


if __name__ == "__main__":
    unittest.main()
