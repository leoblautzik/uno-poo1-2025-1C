"""
Implementar una clase llamada Scrabble que permita calcular el
peso total de una palabra, según los valores clásicos de
las letras en el juego Scrabble.
"""


class Scrabble:
    """La clase debe tener un atributo de clase llamado PESOS,
    que almacene en un diccionario los valores de cada letra:"""

    PESOS: dict[str, int] = {
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
        "ñ": 8,
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
        No debe modificar la palabra.
        Debe funcionar correctamente aunque la palabra contenga símbolos o números.
        """
        peso = 0
        palabra = palabra.strip()
        palabra = palabra.lower()
        for c in palabra:
            if c.isalpha():
                peso += Scrabble.PESOS[c]

        return peso

    def encontrar_ganador(self, scrabbleros: dict[str, list[str]]) -> list[str]:
        """Implementar de manera tal que se reciba un diccionario donde la
        key es el nombre del jugador, y el value la lista de palabras que
        presentó en el tablero durante el juego.
        Debe encontrar al jugador (o jugadores) que logró mayor puntaje.
        En caso de empate, los muestra a todos"""
        ganadores: list[str] = []
        puntajes: dict[str, int] = {}

        for jugador, lista_p in scrabbleros.items():
            puntaje = 0
            for palabra in lista_p:
                puntaje += self.peso_palabra(palabra)

            puntajes[jugador] = puntaje

        puntaje_max = max(puntajes.values())
        # for jugador, puntaje in puntajes.items():
        #     if puntaje > puntaje_max:
        #         puntaje_max = puntaje

        if puntaje_max == 0:
            return []

        for jugador, puntaje in puntajes.items():
            if puntaje == puntaje_max:
                ganadores.append(jugador)

        return ganadores


def main():
    pass


if __name__ == "__main__":
    main()
