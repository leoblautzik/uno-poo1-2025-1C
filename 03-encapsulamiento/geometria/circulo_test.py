import unittest
from circulo import Circulo
from punto import Punto


class TestCirculo(unittest.TestCase):
    def test_intersectan(self):
        c1 = Circulo(Punto(0, 0), 1)
        c2 = Circulo(Punto(1, 1), 1.5)
        self.assertTrue(c1.intersecta_con(c2))

        c3 = Circulo(Punto(0, 0), 2)
        c4 = Circulo(Punto(3, 0), 1)
        self.assertTrue(c3.intersecta_con(c4))

        # Tangencia externa
        c5 = Circulo(Punto(0, 0), 2)
        c6 = Circulo(Punto(4, 0), 2)
        self.assertTrue(c5.intersecta_con(c6))

        # Tangencia interna
        c7 = Circulo(Punto(0, 0), 5)
        c8 = Circulo(Punto(3, 0), 2)
        self.assertTrue(c7.intersecta_con(c8))

        # Un círculo dentro de otro sin tocar
        c3 = Circulo(Punto(0, 0), 5)
        c4 = Circulo(Punto(0, 0), 1)
        self.assertTrue(c3.intersecta_con(c4))

    def test_no_intersectan(self):
        c1 = Circulo(Punto(0, 0), 1)
        c2 = Circulo(Punto(5, 0), 1)
        self.assertFalse(c1.intersecta_con(c2))

        # Muy separados
        c5 = Circulo(Punto(-10, -10), 2)
        c6 = Circulo(Punto(10, 10), 2)
        self.assertFalse(c5.intersecta_con(c6))


if __name__ == "__main__":
    unittest.main()
