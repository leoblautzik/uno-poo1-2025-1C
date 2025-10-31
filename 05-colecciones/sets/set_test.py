"""Casos de prueba para los ejercicios de conjuntos"""

import unittest
from sets import (
    elementos_unicos,
    todos_pares,
    interseccion_unica,
    diferencia_simetrica,
    tiene_elemento_comun,
)


class TestSets(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_elementos_unicos(self):
        self.assertEqual(elementos_unicos([1, 2, 2, 3, 1]), {1, 2, 3})
        self.assertEqual(elementos_unicos([]), set())
        self.assertEqual(elementos_unicos([5, 5, 5]), {5})

    def test_todos_pares(self):
        self.assertTrue(todos_pares({2, 4, 6, 8}))
        self.assertFalse(todos_pares({1, 2, 3}))
        self.assertTrue(todos_pares(set()))  # vacío -> True

    def test_interseccion_unica(self):
        a, b = {1, 2, 3}, {3, 4, 5}
        res = interseccion_unica(a, b)
        self.assertEqual(res, {3})
        self.assertEqual(a, {1, 2, 3})
        self.assertEqual(b, {3, 4, 5})
        self.assertEqual(interseccion_unica(set(), {1, 2}), set())

    def test_diferencia_simetrica(self):
        self.assertEqual(diferencia_simetrica({"a", "b"}, {"b", "c"}), {"a", "c"})
        self.assertEqual(diferencia_simetrica(set(), {"x"}), {"x"})
        self.assertEqual(diferencia_simetrica({"p"}, {"p"}), set())

    def test_tiene_elemento_comun(self):
        self.assertTrue(tiene_elemento_comun([{1, 2}, {2, 3}, {2, 4}]))
        self.assertFalse(tiene_elemento_comun([{1, 2}, {3, 4}]))
        self.assertFalse(tiene_elemento_comun([]))
        self.assertTrue(tiene_elemento_comun([{1, 2, 3}]))


if __name__ == "__main__":
    unittest.main()
