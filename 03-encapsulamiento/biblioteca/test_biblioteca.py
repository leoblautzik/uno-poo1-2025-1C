import unittest

from biblioteca import Biblioteca
from genero import Genero
from libro import Libro


class TestBiblioteca(unittest.TestCase):
    def test_agregar_libro(self):
        mi_biblioteca = Biblioteca()

        mi_biblioteca.agregar_libro("Moby Dick", "Melville", Genero.NOVELA, 1000)
        self.assertEqual(1, mi_biblioteca.cuantos_libros())
        self.assertEqual("Moby Dick", mi_biblioteca.libro_en_la_posicion(1))

    def test_mas_paginas(self):
        mi_biblioteca = Biblioteca()

        mi_biblioteca.agregar_libro("Moby Dick", "Melville", Genero.NOVELA, 1000)
        mi_biblioteca.agregar_libro(
            "El principito", "Antoine de Saint-Exupéry ", Genero.NOVELA, 200
        )
        self.assertEqual(2, mi_biblioteca.cuantos_libros())
        esperado = Libro("Moby Dick", "Melville", Genero.NOVELA, 1000)
        self.assertEqual(esperado, mi_biblioteca.libro_con_mas_paginas())


if __name__ == "__main__":
    unittest.main()
