import unittest
from scrabble import Scrabble  # asumimos que tu clase está en scrabble.py


class TestScrabble(unittest.TestCase):
    def setUp(self):
        self.s = Scrabble()

    def test_palabra_simple(self):
        self.assertEqual(self.s.peso_palabra("hola"), 10)

    def test_palabra_con_mayusculas(self):
        self.assertEqual(self.s.peso_palabra("HOLA"), 10)

    def test_palabra_mixta(self):
        self.assertEqual(self.s.peso_palabra("HoLa"), 10)

    def test_palabra_con_simbolos(self):
        # Ignora símbolos y signos
        self.assertEqual(self.s.peso_palabra("m@r!a"), 5)

    def test_palabra_con_numeros(self):
        # Ignora números
        self.assertEqual(
            self.s.peso_palabra("c4s4"), 5
        )  # c+a+s+a = 3+1+1+1=6 (ups revisar)
        self.assertEqual(self.s.peso_palabra("c4s4"), 6)

    def test_palabra_con_letra_valiosa(self):
        # 'quiz' → q(10) + u(1) + i(1) + z(10) = 22
        self.assertEqual(self.s.peso_palabra("quiz"), 22)

    def test_palabra_vacia(self):
        self.assertEqual(self.s.peso_palabra(""), 0)

    def test_solo_caracteres_invalidos(self):
        self.assertEqual(self.s.peso_palabra("1234!?"), 0)

    def test_todas_las_letras_distintas(self):
        # Asegura que todas las letras del diccionario funcionen
        palabra = "".join(Scrabble.PESOS.keys())
        esperado = sum(Scrabble.PESOS.values())
        self.assertEqual(self.s.peso_palabra(palabra), esperado)

    def test_letra_fuera_del_diccionario(self):
        # Si alguna letra no está en PESOS, debe contarse como 0
        # (por ejemplo, 'ñ' o caracteres especiales)
        self.assertEqual(self.s.peso_palabra("año"), 1 + 0 + 1)

    def test_palabra_larga(self):
        palabra = "supercalifragilistico"
        # Se espera que no falle por longitud
        self.assertIsInstance(self.s.peso_palabra(palabra), int)


if __name__ == "__main__":
    unittest.main()
