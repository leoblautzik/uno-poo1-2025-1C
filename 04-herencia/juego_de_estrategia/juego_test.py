import unittest

from soldado import Soldado


class TestJuego(unittest.TestCase):
    def test_soldado_ataca_soldado(self):
        rambo = Soldado(1)
        ryan = Soldado(1)
        rambo.atacar(ryan)
        self.assertTrue(rambo.puede_atacar(ryan))
        self.assertTrue(ryan.puede_atacar(rambo))

    def test_ataca_hasta_quedar_sin_energia(self):
        rambo = Soldado(1)
        ryan = Soldado(1)

        for _ in range(10):
            rambo.atacar(ryan)

        self.assertEqual(0, rambo.energia)
        self.assertEqual(100, ryan.salud)


if __name__ == "__main__":
    unittest.main()
