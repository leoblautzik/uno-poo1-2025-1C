import unittest
from cerradura import Cerradura


class TestCerradura(unittest.TestCase):
    def test_crear_cerradura(self):
        trabex = Cerradura(123456, 3)
        self.assertTrue(trabex.esta_abierta())
        self.assertFalse(trabex.fue_bloqueada())
        self.assertEqual(0, trabex.contar_aperturas_exitosas())
        self.assertEqual(0, trabex.contar_aperturas_fallidas())

    def test_cerrada_apertura_exitosa(self):
        trabex = Cerradura(123456, 3)
        trabex.cerrar()
        self.assertTrue(trabex.esta_cerrada())
        self.assertTrue(trabex.abrir(123456))
        self.assertTrue(trabex.esta_abierta())
        self.assertEqual(1, trabex.contar_aperturas_exitosas())
        self.assertEqual(0, trabex.contar_aperturas_fallidas())

    def test_cerrada_apertura_fallida(self):
        trabex = Cerradura(123456, 3)
        trabex.cerrar()
        self.assertTrue(trabex.esta_cerrada())
        self.assertFalse(trabex.abrir(123356))
        self.assertFalse(trabex.esta_abierta())
        self.assertEqual(0, trabex.contar_aperturas_exitosas())
        self.assertEqual(1, trabex.contar_aperturas_fallidas())

    def test_cerrada_apertura_fallida_sin_bloquear(self):
        trabex = Cerradura(123456, 3)
        trabex.cerrar()
        self.assertTrue(trabex.esta_cerrada())
        trabex.abrir(123356)
        trabex.abrir(223356)
        self.assertFalse(trabex.esta_abierta())
        self.assertEqual(0, trabex.contar_aperturas_exitosas())
        self.assertEqual(2, trabex.contar_aperturas_fallidas())
        trabex.abrir(123456)
        self.assertTrue(trabex.esta_abierta())
        self.assertEqual(1, trabex.contar_aperturas_exitosas())

    def test_cerrada_apertura_fallida_con_bloqueo(self):
        trabex = Cerradura(123456, 3)
        trabex.cerrar()
        self.assertTrue(trabex.esta_cerrada())
        trabex.abrir(123356)
        trabex.abrir(123356)
        trabex.abrir(223356)
        self.assertFalse(trabex.esta_abierta())
        self.assertEqual(0, trabex.contar_aperturas_exitosas())
        self.assertEqual(3, trabex.contar_aperturas_fallidas())
        self.assertTrue(trabex.fue_bloqueada)
        with self.assertRaises(RuntimeWarning):
            trabex.abrir(123456)
        with self.assertRaises(RuntimeWarning):
            trabex.abrir(23456)


if __name__ == "__main__":
    unittest.main()
