import unittest

# Importar las clases del módulo principal (ajustar el nombre si se guarda en otro archivo)
from juego_estrategia import Soldado, Arquero, Lancero, Caballero


class TestUnidades(unittest.TestCase):
    def setUp(self):
        self.soldado = Soldado(posicion=0)
        self.arquero = Arquero(posicion=3)
        self.lancero = Lancero(posicion=2)
        self.caballero = Caballero(posicion=5)

    def test_soldado_puede_atacar_cercano(self):
        # Distancia = 2 → debería ser False
        self.assertFalse(self.soldado.puede_atacar(self.lancero))
        # Muevo al lancero para que esté a distancia 1
        self.lancero.posicion = 1
        self.assertTrue(self.soldado.puede_atacar(self.lancero))

    def test_arquero_distancia_correcta(self):
        # Distancia = 2 → válido
        self.caballero.posicion = 5
        self.arquero.posicion = 3
        self.assertTrue(self.arquero.puede_atacar(self.caballero))
        # Distancia = 1 → inválido
        self.caballero.posicion = 4
        self.assertFalse(self.arquero.puede_atacar(self.caballero))

    def test_lancero_distancia(self):
        # Distancia = 1 → válido
        self.lancero.posicion = 1
        self.assertTrue(self.lancero.puede_atacar(self.soldado))
        # Distancia = 4 → inválido
        self.lancero.posicion = 4
        self.assertFalse(self.lancero.puede_atacar(self.soldado))

    def test_caballero_caballo_rebelde(self):
        # Distancia = 2 → válido
        self.caballero.posicion = 2
        self.assertTrue(self.caballero.puede_atacar(self.soldado))
        # Simular 3 ataques → caballo rebelde
        for _ in range(3):
            self.caballero.atacar(self.soldado)
        self.assertTrue(self.caballero.caballo_rebelde)
        self.assertFalse(self.caballero.puede_atacar(self.soldado))
        # Luego recibe agua → vuelve a poder atacar
        self.caballero.recibir_agua()
        self.assertTrue(self.caballero.puede_atacar(self.soldado))

    def test_no_ataca_unidad_muerta(self):
        self.soldado.salud = 0
        self.assertFalse(self.soldado.esta_viva())
        self.assertFalse(self.soldado.puede_atacar(self.lancero))


class TestUnidadesReduccionSalud(unittest.TestCase):
    def setUp(self):
        self.soldado = Soldado(posicion=0)
        self.arquero = Arquero(posicion=3)
        self.lancero = Lancero(posicion=1)
        self.caballero = Caballero(posicion=2)

    def test_soldado_puede_atacar_cercano(self):
        self.assertTrue(self.soldado.puede_atacar(self.lancero))
        self.lancero.posicion = 3  # distancia 3 → inválido
        self.assertFalse(self.soldado.puede_atacar(self.lancero))

    def test_arquero_distancia_correcta(self):
        # Distancia 2 → válido
        self.caballero.posicion = 5
        self.arquero.posicion = 3
        self.assertTrue(self.arquero.puede_atacar(self.caballero))
        # Distancia 1 → inválido
        self.caballero.posicion = 4
        self.assertFalse(self.arquero.puede_atacar(self.caballero))

    def test_lancero_distancia(self):
        self.lancero.posicion = 1
        self.assertTrue(self.lancero.puede_atacar(self.soldado))
        self.lancero.posicion = 5
        self.assertFalse(self.lancero.puede_atacar(self.soldado))

    def test_caballero_caballo_rebelde(self):
        self.caballero.posicion = 1
        self.assertTrue(self.caballero.puede_atacar(self.soldado))
        # Simular 3 ataques
        for _ in range(3):
            self.caballero.atacar(self.soldado)
        self.assertTrue(self.caballero.caballo_rebelde)
        self.assertFalse(self.caballero.puede_atacar(self.soldado))
        # Recibir agua
        self.caballero.recibir_agua()
        self.assertTrue(self.caballero.puede_atacar(self.soldado))

    def test_no_ataca_unidad_muerta(self):
        self.soldado.salud = 0
        self.assertFalse(self.soldado.esta_viva())
        self.assertFalse(self.soldado.puede_atacar(self.lancero))

    def test_reduccion_salud_en_ataque(self):
        # Soldado ataca a Lancero
        salud_inicial = self.lancero.salud
        self.lancero.posicion = 1
        if self.soldado.puede_atacar(self.lancero):
            self.soldado.atacar(self.lancero)
        self.assertLess(self.lancero.salud, salud_inicial)

        # Arquero ataca a Caballero
        salud_inicial = self.caballero.salud
        self.arquero.posicion = 0
        self.caballero.posicion = 3  # distancia 3 → válido
        if self.arquero.puede_atacar(self.caballero):
            self.arquero.atacar(self.caballero)
        self.assertLess(self.caballero.salud, salud_inicial)


if __name__ == "__main__":
    unittest.main()
