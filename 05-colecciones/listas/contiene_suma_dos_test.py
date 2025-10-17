import unittest
from listas import contiene_suma_dos  # asumiendo que la función está en main.py


class TestContieneSumaDos(unittest.TestCase):
    """Pruebas unitarias con cobertura completa para contiene_suma_dos."""

    def test_lista_vacia(self):
        """Una lista vacía no puede cumplir la condición."""
        self.assertFalse(contiene_suma_dos([]))

    def test_lista_un_elemento(self):
        """Una lista con un solo elemento no puede formar una suma."""
        self.assertFalse(contiene_suma_dos([5]))

    def test_lista_dos_elementos_no_suma(self):
        """Dos elementos cuya suma no pertenece a la lista deben dar False."""
        self.assertFalse(contiene_suma_dos([2, 7]))

    def test_lista_dos_elementos_con_suma_en_lista(self):
        """Si hay dos elementos y su suma también está, devuelve True."""
        self.assertTrue(contiene_suma_dos([2, 3, 5]))

    def test_caso_del_ejemplo(self):
        """El ejemplo [1, 2, 3, 4, 5] debe devolver True (1+2=3, etc)."""
        self.assertTrue(contiene_suma_dos([1, 2, 3, 4, 5]))

    def test_negativos_y_positivos(self):
        """Debe funcionar correctamente con números negativos."""
        # -2 + 5 = 3 está en la lista
        self.assertTrue(contiene_suma_dos([-2, 5, 3, 10]))

    def test_solo_negativos_sin_suma(self):
        """Lista de negativos sin combinaciones válidas."""
        self.assertFalse(contiene_suma_dos([-10, -5, -3, -1]))

    def test_solo_negativos_con_suma_valida(self):
        """Negativos donde la suma está presente (-5 + -2 = -7)."""
        self.assertTrue(contiene_suma_dos([-5, -2, -7, -1]))

    def test_con_ceros(self):
        """Debe manejar correctamente ceros."""
        # 0 + 0 = 0, por lo tanto debe ser True
        self.assertTrue(contiene_suma_dos([0, 1, 2]))
        self.assertTrue(contiene_suma_dos([0, 0]))  # par de ceros
        self.assertFalse(contiene_suma_dos([0]))  # solo un cero

    def test_con_repetidos(self):
        """Si hay repetidos, debe considerarlos como posibles pares distintos."""
        # 2 + 2 = 4, 4 está en la lista
        self.assertTrue(contiene_suma_dos([2, 2, 4]))

    def test_suma_no_presente(self):
        """Si ninguna suma de pares aparece en la lista, devuelve False."""
        self.assertFalse(contiene_suma_dos([1, 5, 9, 13]))

    def test_lista_grande_con_suma(self):
        """Escenario grande con al menos una combinación válida."""
        lista = list(range(1000))  # 0..999, seguro hay muchas sumas válidas
        self.assertTrue(contiene_suma_dos(lista))

    def test_lista_grande_sin_suma(self):
        """Escenario grande pero sin sumas presentes (solo múltiplos de 100)."""
        lista = [0, 100, 200, 300]
        # 100+200=300 está, entonces True
        self.assertTrue(contiene_suma_dos(lista))
        lista = [0, 100, 400, 900]  # ninguna suma aparece
        self.assertFalse(contiene_suma_dos(lista))

    def test_lista_palindroma_sin_suma(self):
        """Lista simétrica sin sumas presentes."""
        self.assertFalse(contiene_suma_dos([1, 3, 5, 3, 1]))

    def test_lista_con_valores_grandes(self):
        """Números grandes, la suma debe calcularse correctamente."""
        self.assertTrue(contiene_suma_dos([1000000, 500000, 1500000]))
        self.assertFalse(contiene_suma_dos([10**9, 10**6, 10**3]))


if __name__ == "__main__":
    unittest.main()
