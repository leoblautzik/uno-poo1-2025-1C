import unittest

from tarjeta_baja import TarjetaBaja


class TestTarjetaBaja(unittest.TestCase):
    def test_crear_tarjeta(self):
        tb = TarjetaBaja(50)
        self.assertEqual(50, tb.obtener_saldo())

    def test_cargar_tarjeta(self):
        tb = TarjetaBaja(50)
        tb.cargar(20)
        self.assertEqual(70, tb.obtener_saldo())

    def test_pagar_colectivo_suficiente(self):
        tb = TarjetaBaja(50)
        tb.pagar_colectivo()
        self.assertEqual(28.50, tb.obtener_saldo())

    def test_pagar_colectivo_insuficiente(self):
        tb = TarjetaBaja(50)
        tb.pagar_colectivo()
        tb.pagar_colectivo()
        tb.pagar_colectivo()
        self.assertEqual(7, tb.obtener_saldo())

    def test_pagar_colectivo_insuficiente_cargo(self):
        tb = TarjetaBaja(50)
        tb.pagar_colectivo()
        tb.cargar(100)
        tb.pagar_colectivo()
        self.assertEqual(107, tb.obtener_saldo())

    def test_contar_viajer_colectivo(self):
        tb = TarjetaBaja(150)
        tb.pagar_colectivo()
        tb.pagar_colectivo()
        tb.pagar_colectivo()
        self.assertEqual(3, tb.contar_viajes_colectivo())
