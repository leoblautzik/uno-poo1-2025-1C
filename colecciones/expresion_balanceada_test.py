import unittest

from expresion_balanceada import ExpresionBalanceada


class TestColeccionesExpresionBalanceada(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

    def test_balanceada_enunciado(self):
        eb = ExpresionBalanceada()
        self.assertTrue(eb.esta_balanceada("[()]{}{[()()]()}"))

    def test_desbalanceada_enunciado(self):
        eb = ExpresionBalanceada()
        self.assertFalse(eb.esta_balanceada("[(])"))

    def test_todos_de_abrir(self):
        eb = ExpresionBalanceada()
        self.assertFalse(eb.esta_balanceada("[{({{{{((((("))

    def test_todos_de_cerrar(self):
        eb = ExpresionBalanceada()
        self.assertFalse(eb.esta_balanceada("))))))))]]]]]]]]]}}}}}}}}"))

    def test_de_cerrar_de_abrir(self):
        eb = ExpresionBalanceada()
        self.assertFalse(eb.esta_balanceada(")("))

    def test_cualquier_cadena(self):
        eb = ExpresionBalanceada()
        self.assertFalse(eb.esta_balanceada("abc"))


if __name__ == "__main__":
    unittest.main()
