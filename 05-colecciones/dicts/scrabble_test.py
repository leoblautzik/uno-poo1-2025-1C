import unittest
from scrabble import Scrabble


class TestScrabble(unittest.TestCase):
    def setUp(self):
        self.s = Scrabble()

    # Peso palabra

    def test_palabra_simple(self):
        self.assertEqual(self.s.peso_palabra("hola"), 7)

    def test_palabra_con_mayusculas(self):
        self.assertEqual(self.s.peso_palabra("HOLA"), 7)

    def test_palabra_mixta(self):
        self.assertEqual(self.s.peso_palabra("HoLa"), 7)

    def test_palabra_con_simbolos(self):
        # Ignora símbolos y signos
        self.assertEqual(self.s.peso_palabra("m@r!a"), 5)

    def test_palabra_con_numeros(self):
        # Ignora números
        self.assertEqual(self.s.peso_palabra("c4s4"), 4)

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
        self.assertEqual(self.s.peso_palabra("año"), 1 + 8 + 1)

    def test_palabra_larga(self):
        palabra = "supercalifragilistico"
        # Se espera que no falle por longitud
        self.assertIsInstance(self.s.peso_palabra(palabra), int)

    # Encontrar ganador

    def test_ganador_unico(self):
        scrabbleros = {
            "Ana": ["hola", "perro"],
            "Luis": ["sol", "mar"],
            "Eva": ["quiz"],
        }
        self.assertEqual(self.s.encontrar_ganador(scrabbleros), ["Eva"])

    def test_empate(self):
        scrabbleros = {"Ana": ["gato"], "Luis": ["dato"]}
        # “gato” y “pato” tienen el mismo peso (7 puntos)
        self.assertCountEqual(self.s.encontrar_ganador(scrabbleros), ["Ana", "Luis"])

    def test_jugador_sin_palabras(self):
        scrabbleros = {"Ana": ["hola"], "Luis": []}
        self.assertEqual(self.s.encontrar_ganador(scrabbleros), ["Ana"])

    def test_todos_sin_palabras(self):
        scrabbleros = {"Ana": [], "Luis": [], "Eva": []}
        self.assertEqual(self.s.encontrar_ganador(scrabbleros), [])

    def test_palabra_vacia_o_invalida(self):
        scrabbleros = {"Ana": [""], "Luis": ["123"], "Eva": ["a"]}
        # “a” = 1 punto, gana Eva
        self.assertEqual(self.s.encontrar_ganador(scrabbleros), ["Eva"])

    def test_mayusculas_minusculas(self):
        scrabbleros = {"Ana": ["Hola"], "Luis": ["HOLA"]}
        # Deben puntuar igual si la función es case-insensitive
        self.assertCountEqual(self.s.encontrar_ganador(scrabbleros), ["Ana", "Luis"])

    def test_varias_palabras_con_distintos_pesos(self):
        scrabbleros = {
            "Ana": ["zzz"],  # 30
            "Luis": ["quiz"],  # 22
            "Eva": ["joy"],  # 16
        }
        self.assertEqual(self.s.encontrar_ganador(scrabbleros), ["Ana"])

    def test_varios_jugadores_y_varias_palabras(self):
        scrabbleros = {
            "Ana": ["hola", "sol", "perro"],  # hola(10) + sol(3) + perro(7) = 20
            "Luis": ["quiz", "jarra"],  # quiz(22) + jarra(15) = 37
            "Eva": ["mago", "zorro", "uva"],  # mago(7) + zorro(17) + uva(6) = 30
            "Tomi": ["zzz", "aa"],  # zzz(30) + aa(2) = 32
            "Lara": ["joy", "kite", "book"],  # joy(16) + kite(8) + book(10) = 34
        }
        # Luis gana con 37 puntos
        self.assertEqual(self.s.encontrar_ganador(scrabbleros), ["Luis"])

    def test_supercalifragilistico(self):
        scrabbleros = {
            "Ana": ["hola", "sol", "perro"],  # hola(10) + sol(3) + perro(7) = 20
            "Luis": ["quiz", "jarra"],  # quiz(22) + jarra(15) = 37
            "Eva": ["mago", "zorro", "uva"],  # mago(7) + zorro(17) + uva(6) = 30
            "Tomi": ["zzz", "aa"],  # zzz(30) + aa(2) = 32
            "Lara": ["joy", "kite", "book"],  # joy(16) + kite(8) + book(10) = 34
            "Bert": [
                "Supercalifragilisticoexpialidoso"
            ],  # palabra larga → puntaje mayor
        }
        # Bert gana por tener la palabra más pesada
        self.assertEqual(self.s.encontrar_ganador(scrabbleros), ["Bert"])


if __name__ == "__main__":
    unittest.main()
