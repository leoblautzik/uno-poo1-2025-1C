import unittest

from guerrero import Soldado, Orco, Elfo


class TestElfo(unittest.TestCase):
    def setUp(self):
        self.elfo = Elfo("Legolas")
        self.soldado = Soldado("Leonidas")
        self.orco = Orco("Gorgul")

    def test_elfo_ataca_soldado(self):
        self.elfo.atacar(self.soldado)
        self.assertEqual(self.soldado.salud, 200 - 15)  # daño de Elfo
        self.assertEqual(self.elfo.energia, 80 - 5)  # costo de ataque

    def test_soldado_ataca_elfo(self):
        self.soldado.atacar(self.elfo)
        self.assertEqual(self.elfo.salud, 120 - 10)
        self.assertEqual(self.soldado.energia, 100 - 10)

    def test_orco_ataca_elfo(self):
        self.orco.atacar(self.elfo)
        self.assertEqual(self.elfo.salud, 120 - 20)
        self.assertEqual(self.orco.energia, 120 - 15)

    def test_elfo_ataca_orco(self):
        self.elfo.atacar(self.orco)
        self.assertEqual(self.orco.salud, 250 - 15)
        self.assertEqual(self.elfo.energia, 80 - 5)

    def test_elfo_sin_energia_no_ataca(self):
        self.elfo.energia = 0
        self.elfo.atacar(self.soldado)
        self.assertEqual(self.soldado.salud, 200)  # no cambia
        self.assertEqual(self.elfo.energia, 0)  # sigue en 0

    def test_elfo_recibe_racion_y_no_supera_max(self):
        self.elfo.energia = 75
        self.elfo.recibir_racion()  # debería llegar a 80 como máximo
        self.assertEqual(self.elfo.energia, 80)

    def test_elfo_puede_matar_orco(self):
        # 12 ataques * 15 = 180 -> orco muere
        for _ in range(15):
            self.elfo.atacar(self.orco)
        self.elfo.recibir_racion()
        for _ in range(2):
            self.elfo.atacar(self.orco)

        self.assertTrue(self.orco.esta_derrotado())
        self.assertEqual(self.elfo.energia, 15)

    def test_combate_elfo_vs_soldado_turnos(self):
        while not self.elfo.esta_derrotado() and not self.soldado.esta_derrotado():
            self.elfo.atacar(self.soldado)
            if not self.soldado.esta_derrotado():
                self.soldado.atacar(self.elfo)
        self.assertTrue(self.elfo.esta_derrotado() or self.soldado.esta_derrotado())

    def test_elfo_vs_soldado_y_orco(self):
        self.elfo.atacar(self.soldado)
        self.soldado.atacar(self.elfo)
        self.elfo.atacar(self.orco)
        self.assertLess(self.soldado.salud, 200)
        self.assertLess(self.orco.salud, 250)


if __name__ == "__main__":
    unittest.main()
