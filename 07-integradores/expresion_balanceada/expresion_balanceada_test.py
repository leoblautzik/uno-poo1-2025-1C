import unittest

from expresion_balanceada import Expresion


class TestExpresionBalanceada(unittest.TestCase):
    def test_ejemplo_valido(self):
        self.assertTrue(Expresion.esta_balanceada("[()]{}{[()()]()}"))

    def test_ejemplo_invalido(self):
        self.assertFalse(Expresion.esta_balanceada("[(])"))

    def test_cadena_vacia(self):
        self.assertTrue(Expresion.esta_balanceada(""))

    def test_un_solo_tipo_balanceado(self):
        self.assertTrue(Expresion.esta_balanceada("(((())))"))

    def test_un_solo_tipo_no_balanceado(self):
        self.assertFalse(Expresion.esta_balanceada("((()"))

    def test_solo_un_cierre_suelto(self):
        self.assertFalse(Expresion.esta_balanceada("]"))

    def test_solo_un_apertura_suelta(self):
        self.assertFalse(Expresion.esta_balanceada("("))

    def test_mezcla_incorrecta_de_simbolos(self):
        self.assertFalse(Expresion.esta_balanceada("{[}]"))

    def test_balanceado_con_muchos_niveles(self):
        self.assertTrue(Expresion.esta_balanceada("{{[[(())]]}}"))

    def test_caracteres_no_relevantes(self):
        # Si tu función ignora caracteres distintos de (){}[], debería devolver True
        self.assertTrue(Expresion.esta_balanceada("a+(b*[c-{d/e}])"))

    def test_inicia_con_cierre(self):
        self.assertFalse(Expresion.esta_balanceada("){[]}"))

    def test_cierre_extra_al_final(self):
        self.assertFalse(Expresion.esta_balanceada("{[]}()()]"))


if __name__ == "__main__":
    unittest.main()
