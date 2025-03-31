"""Pruebas unitarias para la Tarjeta Baja"""

import unittest

from tarjeta_baja import TarjetaBaja


class TarjetaBajaTest(unittest.TestCase):
    """Pruebas unitarias TarjetaBaja"""

    def test_obtener_saldo(self):
        """obtener_saldo test"""
        tb = TarjetaBaja(2000)
        esperado = 2000
        obtenido = tb.obtener_saldo()
        self.assertEqual(esperado, obtenido)

    def test_pagar_colectivo(self):
        tb = TarjetaBaja(50)
        tb.pagar_viaje_en_colectivo()
        esperado = 28.50
        obtenido = tb.obtener_saldo()
        self.assertEqual(esperado, obtenido)


if __name__ == "__main__":
    unittest.main()
