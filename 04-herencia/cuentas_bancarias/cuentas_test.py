"""Pruebas unitarias para Circulo"""

import unittest

from cuenta_ahorro import CajaDeAhorro
from cuenta_corriente import CuentaCorriente


class CuentasTest(unittest.TestCase):
    """Pruebas unitarias Cuentas bancarias"""

    def test_caja_ahorro(self):
        """saldo test"""
        ca = CajaDeAhorro(123)
        esperado = 0.0
        obtenido = ca.get_saldo()
        self.assertEqual(esperado, obtenido)

    def test_depositar_caja_ahorro(self):
        """depositar en una nueva caja de ahorro y verificar el saldo"""
        ca = CajaDeAhorro(123)
        ca.depositar(10000)
        self.assertEqual(10000, ca.get_saldo())

    def test_transferir(self):
        """saldo en dos cuentas luego de hacer una transferencia"""
        ca = CajaDeAhorro(123)
        ca.depositar(10000)
        cc = CuentaCorriente(234, 10000)
        cc.depositar(1000)
        ca.transferir(cc, 5000)
        self.assertEqual(5000, ca.get_saldo())
        self.assertEqual(6000, cc.get_saldo())

    def test_cta_cte(self):
        cc = CuentaCorriente(123456, 1000)
        cc.extraer(500)
        self.assertEqual(-500, cc.get_saldo())
        cc.extraer(500)
        self.assertEqual(-1000, cc.get_saldo())
        cc.extraer(500)
        self.assertEqual(-1000, cc.get_saldo())
        print(cc)


if __name__ == "__main__":
    unittest.main()
