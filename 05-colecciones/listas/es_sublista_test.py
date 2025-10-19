import unittest
from listas import es_sublista  # suponiendo que la función está en main.py


class TestEsSublista(unittest.TestCase):
    """Casos de prueba con buena cobertura para es_sublista."""

    def test_sublista_en_medio(self):
        """Caso del ejemplo: sublista en el medio de la lista principal."""
        l1 = [22, 14, 6]
        l2 = [39, 41, 17, 22, 14, 6, 3, 11, 73, 81]
        self.assertTrue(es_sublista(l1, l2))

    def test_no_es_sublista_por_desorden(self):
        """Mismos elementos pero en orden distinto: no es sublista."""
        l1 = [22, 14, 6]
        l3 = [39, 41, 22, 17, 14, 3, 11, 73, 6, 81]
        self.assertFalse(es_sublista(l1, l3))

    def test_sublista_al_principio(self):
        """Sublista que aparece al principio de la lista mayor."""
        self.assertTrue(es_sublista([1, 2, 3], [1, 2, 3, 4, 5]))

    def test_sublista_al_final(self):
        """Sublista que aparece al final de la lista mayor."""
        self.assertTrue(es_sublista([4, 5, 6], [0, 1, 2, 3, 4, 5, 6]))

    def test_sublista_igual(self):
        """Si las listas son iguales, l1 es sublista de l2."""
        self.assertTrue(es_sublista([10, 20, 30], [10, 20, 30]))

    def test_sublista_vacia(self):
        """Una lista vacía siempre es sublista de cualquier otra."""
        self.assertTrue(es_sublista([], [1, 2, 3]))

    def test_lista_principal_vacia(self):
        """Una lista no vacía nunca puede ser sublista de una vacía."""
        self.assertFalse(es_sublista([1, 2, 3], []))

    def test_ambas_vacias(self):
        """Dos listas vacías: True por definición (sublista trivial)."""
        self.assertTrue(es_sublista([], []))

    def test_un_elemento_presente(self):
        """Sublista de un solo elemento presente en l2."""
        self.assertTrue(es_sublista([7], [1, 7, 3, 5]))

    def test_un_elemento_ausente(self):
        """Sublista de un solo elemento que no está en l2."""
        self.assertFalse(es_sublista([8], [1, 7, 3, 5]))

    def test_elementos_repetidos_consecutivos(self):
        """Manejo de repeticiones consecutivas."""
        # La sublista [2, 2, 3] aparece explícitamente
        self.assertTrue(es_sublista([2, 2, 3], [1, 2, 2, 3, 4]))
        # Pero [2, 3, 3] no aparece en ese orden
        self.assertFalse(es_sublista([2, 3, 3], [1, 2, 2, 3, 4]))

    def test_sublista_parcial_con_repetidos(self):
        """Evita falsos positivos por repeticiones."""
        # [2, 3, 2] no está en [2, 2, 3, 2]
        self.assertTrue(es_sublista([2, 3, 2], [2, 2, 3, 2]))

    def test_sublista_mas_larga_que_lista(self):
        """Una sublista más larga que la lista principal no puede estar incluida."""
        self.assertFalse(es_sublista([1, 2, 3, 4], [1, 2, 3]))

    def test_sublista_con_valores_negativos(self):
        """Debe funcionar con enteros negativos."""
        self.assertTrue(es_sublista([-2, -1], [0, -3, -2, -1, 5]))
        self.assertFalse(es_sublista([-2, -1], [-3, -1, -2, 5]))

    def test_sublista_en_medio_con_numeros_grandes(self):
        """Debe manejar números grandes sin problema."""
        self.assertTrue(
            es_sublista([1000000, 2000000], [10, 1000000, 2000000, 3000000])
        )

    def test_sublista_repetida_multiples_veces(self):
        """Si aparece varias veces, debe detectar correctamente al menos una."""
        self.assertTrue(es_sublista([3, 4], [1, 2, 3, 4, 3, 4, 5]))

    def test_no_falsa_coincidencia_parcial(self):
        """Evita coincidir parcialmente al reiniciar búsqueda."""
        # [1, 2, 1, 2, 3] está, pero [1, 2, 3, 1, 2] no.
        self.assertFalse(es_sublista([1, 2, 3, 1, 2], [1, 2, 1, 2, 3, 4, 5]))


if __name__ == "__main__":
    unittest.main()
