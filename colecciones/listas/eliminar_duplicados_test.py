import unittest
from listas import eliminar_duplicados  # asumiendo que la función está en main.py


class TestEliminarDuplicados(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(eliminar_duplicados([]), [])

    def test_sin_duplicados(self):
        self.assertEqual(eliminar_duplicados([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_con_duplicados_simples(self):
        self.assertEqual(eliminar_duplicados([1, 2, 2, 1, 4, 2, 4, 3]), [1, 2, 4, 3])

    def test_todos_iguales(self):
        self.assertEqual(eliminar_duplicados([5, 5, 5, 5, 5]), [5])

    def test_duplicados_no_consecutivos(self):
        self.assertEqual(eliminar_duplicados([1, 2, 3, 1, 2, 4]), [1, 2, 3, 4])

    def test_orden_conservado(self):
        self.assertEqual(eliminar_duplicados([4, 1, 4, 2, 1, 3, 4]), [4, 1, 2, 3])

    def test_numeros_negativos(self):
        self.assertEqual(eliminar_duplicados([-1, -2, -1, 0, -2, 3]), [-1, -2, 0, 3])

    def test_grandes_y_ceros(self):
        self.assertEqual(
            eliminar_duplicados([0, 0, 999999, 1, 999999, 0]), [0, 999999, 1]
        )

    def test_tipo_inmutable_no_altera_original(self):
        datos = [1, 2, 2, 3]
        copia = list(datos)
        eliminar_duplicados(datos)
        self.assertEqual(datos, copia)

    def test_lista_larga(self):
        datos = [i % 10 for i in range(1000)]
        esperado = list(range(10))
        self.assertEqual(eliminar_duplicados(datos), esperado)


if __name__ == "__main__":
    unittest.main()
