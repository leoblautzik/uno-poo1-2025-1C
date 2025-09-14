"""Atributos:
nombre → identificador de la nave.
salud → puntos de vida de la nave.
danio → puntos de salud que provoca en su oponente cuando ataca

Métodos:
atacar(otra) → será redefinido en las subclases.
recibir_danio(atacante) → resta salud a la nave de acuerdo a quien la ataca
(no puede bajar de 0).
esta_destruida() → devuelve True si la salud llega a 0 o menos.
estado() → devuelve un string con nombre y salud actual.
"""

from __future__ import annotations


class Nave:
    def __init__(self, nombre, salud, danio) -> None:
        self.__nombre = nombre
        self.__salud = salud
        self.__danio = danio

    def atacar(self, otra: Nave) -> None:
        pass

    def recibir_danio(self, otra: Nave) -> None:
        pass

    def esta_destruida(self) -> bool:
        pass

    def estado(self) -> str:
        pass


class Caza(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=100, danio=15)

    def atacar(self, otra: Nave) -> None:
        pass


class Bombardero(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=150, danio=25)

    def atacar(self, otra: Nave) -> None:
        """TODO Inflige 25 de daño y recibe 5 de autodaño."""
        pass


class Crucero(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=300, danio=40)

    def atacar(self, otra: Nave) -> None:
        """TODO Inflige 40 de daño si la salud > 50, en caso contrario no ataca."""
        pass


def main():
    pass


if __name__ == "__main__":
    main()
