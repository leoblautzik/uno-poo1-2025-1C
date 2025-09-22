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

    @property
    def nombre(self):
        return self.__nombre

    @property
    def danio(self):
        return self.__danio

    @danio.setter
    def danio(self, d):
        self.__danio = d

    @property
    def salud(self):
        return self.__salud

    @salud.setter
    def salud(self, s):
        self.__salud = s

    def atacar(self, otra: Nave) -> None:
        pass

    def recibir_danio(self, atacante: Nave) -> None:
        self.salud -= atacante.danio
        if self.salud < 0:
            self.salud = 0

    def esta_destruida(self) -> bool:
        return self.__salud == 0

    def estado(self) -> str:
        return f"Nave: {self.nombre} -> salud: {self.salud}"


class Caza(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=100, danio=15)

    def atacar(self, otra: Nave) -> None:
        otra.recibir_danio(self)


class Bombardero(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=150, danio=25)

    def atacar(self, otra: Nave) -> None:
        """Inflige 25 de daño y recibe 5 de autodaño."""
        otra.recibir_danio(self)
        self.salud -= 5


class Crucero(Nave):
    def __init__(self, nombre: str):
        super().__init__(nombre, salud=300, danio=40)

    def atacar(self, otra: Nave) -> None:
        """Inflige 40 de daño si la salud > 50, en caso contrario no ataca."""
        if self.salud > 50:
            otra.recibir_danio(self)


class Blindado:
    """Reduce el daño recibido en un 20%."""

    def danio_reducido(self, atacante: Nave):
        return atacante.danio * 0.8


class Camuflado:
    def esquivar(self) -> bool:
        """Tiene un 30% de probabilidad de esquivar el ataque."""
        import random

        return random.random() < 0.3


class BombarderoBlindado(Bombardero, Blindado):
    def recibir_danio(self, atacante: "Nave") -> None:
        # se reduce el daño usando Blindado

        self.salud -= self.danio_reducido(atacante)
        if self.salud < 0:
            self.salud = 0


class CazaCamuflado(Caza, Camuflado):
    def recibir_danio(self, atacante: "Nave") -> None:
        # puede esquivar el ataque
        if self.esquivar():
            return  # esquivó, no recibe daño
        self.salud -= atacante.danio
        if self.salud < 0:
            self.salud = 0


class BombarderoCamuflado(Bombardero, Camuflado):
    def recibir_danio(self, atacante: "Nave") -> None:
        # puede esquivar el ataque
        if self.esquivar():
            return  # esquivó, no recibe daño
        self.salud -= atacante.danio
        if self.salud < 0:
            self.salud = 0


def main():
    pass


if __name__ == "__main__":
    main()
