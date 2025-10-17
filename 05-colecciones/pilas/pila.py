from typing import dataclass_transform


class Pila:
    def __init__(self):
        self.__p = []

    def apilar(self, dato):
        self.__p.append(dato)

    def desapilar(self):
        if not self.vacia():
            return self.__p.pop()

    def vacia(self):
        return len(self.__p) == 0

    def tope(self):
        return self.__p[len(self.__p) - 1]

    def clear(self):
        self.__p.clear()


class Cadena:
    @classmethod
    def invertir_cadena(cls, cadena: str) -> str:
        s = ""
        p = Pila()
        for c in cadena:
            p.apilar(c)

        while not p.vacia():
            s += str(p.desapilar())
        return s

    @classmethod
    def es_palindromo(cls, cadena: str) -> bool:
        return cadena == cls.invertir_cadena(cadena)


def main():
    print(Cadena.invertir_cadena("Hola Mundo"))
    print(Cadena.es_palindromo("NEUQUEN"))


if __name__ == "__main__":
    main()
