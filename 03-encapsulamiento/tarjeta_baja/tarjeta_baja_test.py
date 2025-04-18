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

    def test_pagar_subte(self):
        tb = TarjetaBaja(50)
        tb.pagar_viaje_en_subte()
        esperado = 30.50
        obtenido = tb.obtener_saldo()
        self.assertEqual(esperado, obtenido)

    def test_cargar(self):
        tb = TarjetaBaja(50)
        tb.cargar(100)
        self.assertEqual(150, tb.obtener_saldo())


if __name__ == "__main__":
    unittest.main()
