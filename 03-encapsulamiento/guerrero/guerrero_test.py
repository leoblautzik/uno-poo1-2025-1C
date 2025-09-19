# test_guerreros.py

import unittest

from guerrero import Orco, Soldado


class TestGuerreros(unittest.TestCase):
    def test_inicializacion_soldado(self):
        s = Soldado("Ares")
        self.assertEqual(s.nombre, "Ares")
        self.assertEqual(s.energia, 100)
        self.assertEqual(s.salud, 200)
        self.assertEqual(s.costo_ataque, 10)
        self.assertEqual(s.danio, 10)
        self.assertEqual(s.energia_max, 100)

    def test_inicializacion_orco(self):
        o = Orco("Grom")
        self.assertEqual(o.nombre, "Grom")
        self.assertEqual(o.energia, 120)
        self.assertEqual(o.salud, 250)
        self.assertEqual(o.costo_ataque, 15)
        self.assertEqual(o.danio, 20)
        self.assertEqual(o.energia_max, 120)

    def test_soldado_ataca_a_orco(self):
        s = Soldado("Ares")
        o = Orco("Grom")
        s.atacar(o)
        self.assertEqual(s.energia, 90)
        self.assertEqual(o.salud, 240)

    def test_orco_ataca_a_soldado(self):
        s = Soldado("Ares")
        o = Orco("Grom")
        o.atacar(s)
        self.assertEqual(o.energia, 105)
        self.assertEqual(s.salud, 180)

    def test_no_puede_atacar_sin_energia(self):
        o = Orco("Grom")
        s = Soldado("Ares")
        o.energia = 15
        o.atacar(s)  # debería gastar la última posible
        o.atacar(s)  # ahora ya no debería poder
        self.assertEqual(0, o.energia)

    def test_recibir_racion_limite(self):
        s = Soldado("Ares")
        s.energia = 95
        s.recibir_racion()
        self.assertEqual(s.energia, 100)

        o = Orco("Grom")
        o.energia = 115
        o.recibir_racion()
        self.assertEqual(o.energia, 120)

    def test_derrota_por_danio_exactamente(self):
        s = Soldado("Ares")
        o = Orco("Grom")
        o.salud = 10
        s.atacar(o)
        self.assertEqual(o.salud, 0)
        self.assertTrue(o.esta_derrotado())

    def test_no_puede_atacar_derrotado(self):
        s = Soldado("Ares")
        o = Orco("Grom")
        o.salud = 0  # ya derrotado
        energia_inicial = o.energia
        s_salud_inicial = s.salud
        o.atacar(s)
        self.assertEqual(o.energia, energia_inicial)
        self.assertEqual(s.salud, s_salud_inicial)

    def test_estado_incluye_nombre_salud_y_energia(self):
        s = Soldado("Ares")
        texto = s.estado()
        self.assertIn("Ares", texto)
        self.assertIn("Salud", texto)
        self.assertIn("Energía", texto)


if __name__ == "__main__":
    unittest.main()
