import unittest
from soldado import Soldado  # asumimos que implementan la clase en soldado.py


class TestSoldado(unittest.TestCase):
    def test_inicializacion(self):
        s = Soldado("Ares")
        self.assertEqual(s.nombre, "Ares")
        self.assertEqual(s.energia, 100)
        self.assertEqual(s.salud, 200)

    def test_ataque_resta_energia_y_salud(self):
        s1 = Soldado("Ares")
        s2 = Soldado("Zeus")
        s1.atacar(s2)
        self.assertEqual(s1.energia, 90)
        self.assertEqual(s2.salud, 190)

    def test_no_puede_atacar_sin_energia(self):
        s1 = Soldado("Ares")
        s2 = Soldado("Zeus")
        # gastar toda la energía
        for _ in range(10):
            s1.atacar(s2)
        # ya sin energía suficiente
        s1.atacar(s2)
        self.assertEqual(s1.energia, 0)
        self.assertEqual(s2.salud, 100)  # solo recibió 10 ataques, no 11

    def test_recibir_racion_suma_energia(self):
        s = Soldado("Ares")
        s.energia = 50
        s.recibir_racion()
        self.assertEqual(s.energia, 70)

    def test_energia_no_supera_100(self):
        s = Soldado("Ares")
        s.recibir_racion()
        self.assertEqual(s.energia, 100)

    def test_salud_llega_a_cero(self):
        s1 = Soldado("Ares")
        s2 = Soldado("Zeus")
        for _ in range(10):
            s1.atacar(s2)
        for _ in range(5):
            s1.recibir_racion()
        for _ in range(10):
            s1.atacar(s2)

    def test_soldado_derrotado(self):
        s1 = Soldado("Ares")
        s2 = Soldado("Zeus")
        for _ in range(10):
            s1.atacar(s2)
        for _ in range(5):
            s1.recibir_racion()
        for _ in range(10):
            s1.atacar(s2)
        self.assertTrue(s2.esta_derrotado())

    def test_estado_devuelve_string(self):
        s = Soldado("Ares")
        estado = s.estado()
        self.assertEqual(estado, "Nombre: Ares, Salud: 200, Energía: 100")

    def test_multiples_raciones(self):
        s = Soldado("Ares")
        s.energia = 40
        s.recibir_racion()
        s.recibir_racion()
        self.assertEqual(s.energia, 80)

    def test_no_puede_atacar_si_esta_derrotado(self):
        s1 = Soldado("Ares")
        s2 = Soldado("Zeus")
        # s1 derrota a s2
        for _ in range(10):
            s1.atacar(s2)
        for _ in range(5):
            s1.recibir_racion()
        for _ in range(10):
            s1.atacar(s2)

        # s2 intenta atacar estando derrotado
        energia_antes = s2.energia
        salud_antes = s1.salud
        s2.atacar(s1)
        self.assertEqual(s2.energia, energia_antes)  # no gasta energía
        self.assertEqual(s1.salud, salud_antes)  # no hace daño

    def test_recibir_racion_en_derrotado(self):
        s = Soldado("Ares")
        s.salud = 0  # ya está derrotado
        energia_inicial = s.energia
        s.recibir_racion()
        # Decide tu política: aquí asumimos que un derrotado
        # no recupera energía
        self.assertEqual(s.energia, energia_inicial)

    def test_estado_con_soldado_derrotado(self):
        s = Soldado("Zeus")
        s.salud = 0
        # El string debería reflejar que está derrotado
        self.assertTrue(s.esta_derrotado())

    def test_ataque_deja_salud_en_cero_exacta(self):
        s1 = Soldado("Ares")
        s2 = Soldado("Zeus")
        s2.salud = 10
        s1.atacar(s2)
        self.assertEqual(s2.salud, 0)
        self.assertTrue(s2.esta_derrotado())


if __name__ == "__main__":
    unittest.main()
