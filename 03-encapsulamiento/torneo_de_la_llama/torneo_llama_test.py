import unittest
from torneo_de_la_llama import Heroe, Item, Torneo


class TestTorneoDeLaLlamaTorneoLlama(unittest.TestCase):
    def test_poder_fuego(self):
        superman = Heroe("Superman")
        chapulin = Heroe("Chapulin Colorado")
        superman.agregar_item(Item.CAPA)
        superman.agregar_item(Item.ESPADA)
        chapulin.agregar_item(Item.VARITA)
        chapulin.agregar_item(Item.CAPA)
        self.assertEqual(15, superman.poder_de_fuego())
        self.assertEqual(12, chapulin.poder_de_fuego())

    def test_quitar_item(self):
        superman = Heroe("Superman")
        superman.agregar_item(Item.CAPA)
        superman.agregar_item(Item.ESPADA)
        print(superman.mostrar_items())
        self.assertEqual(15, superman.poder_de_fuego())
        superman.consumir_item(Item.ESPADA)
        self.assertEqual(5, superman.poder_de_fuego())
        print(superman.mostrar_items())

    def test_enfrentamiento(self):
        superman = Heroe("Superman")
        chapulin = Heroe("Chapulin Colorado")
        superman.agregar_item(Item.CAPA)
        superman.agregar_item(Item.ESPADA)
        chapulin.agregar_item(Item.VARITA)
        chapulin.agregar_item(Item.CAPA)
        self.assertEqual(15, superman.poder_de_fuego())
        self.assertEqual(12, chapulin.poder_de_fuego())

        la_llama = Torneo()
        la_llama.agregar_heroe(superman)
        la_llama.agregar_heroe(chapulin)

        la_llama.enfrentar(superman, chapulin)
        self.assertEqual(0, superman.poder_de_fuego())
        self.assertEqual(0, chapulin.poder_de_fuego())


if __name__ == "__main__":
    unittest.main()
