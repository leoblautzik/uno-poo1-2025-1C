# test_cuenta.py
import unittest

from cuenta import CuentaBancaria


class TestCuentaBancaria(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n==> setUpClass: se ejecuta UNA SOLA VEZ antes de todos los tests")
        cls.datos_globales = {"moneda": "ARS"}  # Ejemplo de recurso compartido

    def setUp(self):
        print("\n--> setUp: se ejecuta ANTES de cada test")
        # Cada test arranca con una cuenta nueva
        self.cuenta = CuentaBancaria(100)

    def test_deposito(self):
        print("Ejecutando test_deposito")
        self.cuenta.depositar(50)
        self.assertEqual(self.cuenta.get_saldo(), 150)

    def test_retiro(self):
        print("Ejecutando test_retiro")
        self.cuenta.retirar(30)
        self.assertEqual(self.cuenta.get_saldo(), 70)

    def test_saldo_inicial(self):
        print("Ejecutando test_saldo_inicial")
        self.assertEqual(self.cuenta.get_saldo(), 100)


if __name__ == "__main__":
    unittest.main()
