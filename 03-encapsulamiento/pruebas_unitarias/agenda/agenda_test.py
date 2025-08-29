import unittest

from agenda import Agenda


class TestAgendaAgenda(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.agenda.agregar_contacto("Ana", "12345")
        self.agenda.agregar_contacto("Luis", "67890")

    def test_agregar_contacto(self):
        # Antes de agregar hay 2
        self.assertEqual(len(self.agenda.listar_contactos()), 2)
        self.agenda.agregar_contacto("Marta", "55555")
        # Ahora hay 3
        self.assertEqual(len(self.agenda.listar_contactos()), 3)
        self.assertIn("Marta: 55555", self.agenda.listar_contactos())

    def test_buscar_contacto_existente(self):
        contacto = self.agenda.buscar_contacto("Ana")
        self.assertIsNotNone(contacto)
        self.assertEqual(contacto.get_nombre(), "Ana")
        self.assertEqual(contacto.get_telefono(), "12345")

    def test_buscar_contacto_inexistente(self):
        contacto = self.agenda.buscar_contacto("Pedro")
        self.assertIsNone(contacto)

    def test_listar_contactos(self):
        lista = self.agenda.listar_contactos()
        self.assertIn("Ana: 12345", lista)
        self.assertIn("Luis: 67890", lista)
        self.assertEqual(len(lista), 2)


if __name__ == "__main__":
    unittest.main()
