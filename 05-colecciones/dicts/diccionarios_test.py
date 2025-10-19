import unittest
from diccionarios import (
    contar_frecuencias,
    invertir_diccionario,
    fusionar_diccionarios,
    filtrar_por_valor,
    clave_mas_larga,
)


class TestDicts(unittest.TestCase):
    def test_contar_frecuencias(self):
        self.assertEqual(
            contar_frecuencias(["uno", "dos", "uno"]), {"uno": 2, "dos": 1}
        )
        self.assertEqual(contar_frecuencias([]), {})
        self.assertEqual(contar_frecuencias(["x"]), {"x": 1})
        # Caso con todas palabras diferentes
        self.assertEqual(contar_frecuencias(["a", "b", "c"]), {"a": 1, "b": 1, "c": 1})
        # Caso con repeticiones múltiples
        self.assertEqual(
            contar_frecuencias(["rojo", "rojo", "azul", "rojo", "azul"]),
            {"rojo": 3, "azul": 2},
        )
        # Caso sensible a mayúsculas (si la función no normaliza)
        self.assertEqual(
            contar_frecuencias(["Hola", "hola", "HOLA"]),
            {"Hola": 1, "hola": 1, "HOLA": 1},
        )
        # Caso con palabras con espacios extra
        # (si la función no limpia strings)
        self.assertEqual(
            contar_frecuencias(["  uno", "uno", "uno  "]),
            {"  uno": 1, "uno": 1, "uno  ": 1},
        )
        # Caso con números o símbolos (para ver si la función maneja tokens mixtos)
        self.assertEqual(
            contar_frecuencias(["1", "2", "1", "!", "!"]), {"1": 2, "2": 1, "!": 2}
        )
        # Caso con palabra repetida no contigua (para confirmar acumulación correcta)
        self.assertEqual(
            contar_frecuencias(["x", "y", "x", "z", "y", "x"]), {"x": 3, "y": 2, "z": 1}
        )

    def test_invertir_diccionario(self):
        entrada = {"hola": 2, "chau": 3, "si": 2}
        esperado = {2: ["hola", "si"], 3: ["chau"]}
        salida = invertir_diccionario(entrada)
        self.assertEqual(
            {k: set(v) for k, v in salida.items()},
            {k: set(v) for k, v in esperado.items()},
        )
        self.assertEqual(invertir_diccionario({}), {})

    def test_fusionar_diccionarios(self):
        a = {"a": 1, "b": 2}
        b = {"b": 3, "c": 4}
        self.assertEqual(fusionar_diccionarios(a, b), {"a": 1, "b": 5, "c": 4})
        self.assertEqual(a, {"a": 1, "b": 2})
        self.assertEqual(b, {"b": 3, "c": 4})
        self.assertEqual(fusionar_diccionarios({}, {"x": 9}), {"x": 9})

    def test_filtrar_por_valor(self):
        self.assertEqual(
            filtrar_por_valor({"a": 5, "b": 2, "c": 8}, 5), {"a": 5, "c": 8}
        )
        self.assertEqual(filtrar_por_valor({}, 10), {})
        self.assertEqual(filtrar_por_valor({"x": 1}, 2), {})

    def test_clave_mas_larga(self):
        self.assertEqual(
            clave_mas_larga({"uno": "1", "tres": "3", "veintidos": "22"}), "veintidos"
        )
        self.assertEqual(clave_mas_larga({}), "")
        self.assertEqual(clave_mas_larga({"a": "b"}), "a")


if __name__ == "__main__":
    unittest.main()
