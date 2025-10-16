import unittest
from listas import invertir_lista  # asumiendo que la función está en main.py


class TestInvertirLista(unittest.TestCase):
    """Pruebas unitarias para invertir_lista con amplia cobertura de casos."""

    def test_lista_vacia(self):
        """Debe devolver una lista vacía si la entrada es vacía."""
        self.assertEqual(invertir_lista([]), [])

    def test_un_elemento(self):
        """Una lista de un solo elemento debe devolverse igual."""
        self.assertEqual(invertir_lista([42]), [42])

    def test_dos_elementos(self):
        """Debe invertir correctamente una lista de dos elementos."""
        self.assertEqual(invertir_lista([1, 2]), [2, 1])

    def test_varios_elementos(self):
        """Debe invertir una lista de varios elementos."""
        self.assertEqual(invertir_lista([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_con_numeros_negativos(self):
        """Debe funcionar con enteros negativos."""
        self.assertEqual(invertir_lista([-5, -2, -1, 0, 3]), [3, 0, -1, -2, -5])

    def test_con_repetidos(self):
        """Debe mantener los elementos repetidos en orden inverso."""
        self.assertEqual(invertir_lista([1, 2, 2, 3, 1]), [1, 3, 2, 2, 1])

    def test_lista_palindroma(self):
        """Una lista que se lee igual al derecho y al revés debe permanecer igual."""
        self.assertEqual(invertir_lista([1, 2, 3, 2, 1]), [1, 2, 3, 2, 1])

    def test_original_no_modificado(self):
        """La función no debe modificar la lista original."""
        datos = [10, 20, 30]
        copia = list(datos)
        invertir_lista(datos)
        self.assertEqual(datos, copia)

    def test_lista_con_ceros(self):
        """Debe funcionar correctamente con ceros intercalados."""
        self.assertEqual(invertir_lista([0, 1, 0, 2, 0]), [0, 2, 0, 1, 0])

    def test_lista_con_valores_grandes(self):
        """Debe invertir correctamente con números grandes."""
        self.assertEqual(
            invertir_lista([1000000, 2000000, 3000000]), [3000000, 2000000, 1000000]
        )

    def test_invertir_dos_veces(self):
        """Invertir dos veces debe devolver la lista original."""
        datos = [5, 10, 15, 20]
        self.assertEqual(invertir_lista(invertir_lista(datos)), datos)

    def test_lista_grande(self):
        """Debe manejar listas largas sin errores."""
        datos = list(range(10000))
        esperado = list(reversed(datos))
        self.assertEqual(invertir_lista(datos), esperado)


if __name__ == "__main__":
    unittest.main()
