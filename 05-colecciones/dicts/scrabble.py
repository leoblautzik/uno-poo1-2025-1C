"""
Implementar una clase llamada Scrabble que permita calcular el
peso total de una palabra, según los valores clásicos de
las letras en el juego Scrabble.
"""


class Scrabble:
    """La clase debe tener un atributo de clase llamado PESOS,
    que almacene en un diccionario los valores de cada letra:"""

    PESOS = {
        "a": 1,
        "b": 3,
        "c": 3,
        "d": 2,
        "e": 1,
        "f": 4,
        "g": 2,
        "h": 4,
        "i": 1,
        "j": 8,
        "k": 5,
        "l": 1,
        "m": 3,
        "n": 1,
        "o": 1,
        "p": 3,
        "q": 10,
        "r": 1,
        "s": 1,
        "t": 1,
        "u": 1,
        "v": 4,
        "w": 4,
        "x": 8,
        "y": 4,
        "z": 10,
    }

    def peso_palabra(self, palabra: str) -> int:
        """Implementar tal que devuelva la suma de los valores de cada letra
        de la palabra recibida, ignorando mayúsculas y cualquier carácter que
        no sea una letra.
        No debe modificar el diccionario original.
        Debe funcionar correctamente aunque la palabra contenga símbolos o números.
        El cálculo no distingue entre mayúsculas y minúsculas.
        """
        # TODO
        return 0


def main():
    pass


if __name__ == "__main__":
    main()
