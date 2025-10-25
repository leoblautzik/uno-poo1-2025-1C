"""Defina una clase Punto que tendrá dos atributos, de tipo float, x e y,
que representarán las coordenadas del punto dentro del plano."""

from __future__ import annotations
from math import hypot, sqrt
from warnings import warn


class Punto:
    """Modela un objeto Punto en el plano XY"""

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        """Devuelve la coordenada X."""
        return self.__x

    @property
    def y(self) -> float:
        """Devuelve la coordenada Y."""
        return self.__y

    def esta_sobre_eje_x(self) -> bool:
        """Devuelve True o False si el punto esta o no, sobre el eje X"""
        return self.__y == 0

    def esta_sobre_eje_y(self) -> bool:
        """Devuelve True o False si el punto esta o no, sobre el eje Y"""
        return self.__x == 0

    def es_el_origen(self) -> bool:
        """Devuelve True o False si el punto es o no,
        el oigen de coordenadas"""
        return self.esta_sobre_eje_x() and self.esta_sobre_eje_y()

    def distancia_al_origen(self) -> float:
        """Devuelve la distancia del punto al origen de coordenadas"""
        return hypot(self.__x, self.__y)

    def distancia(self, p: "Punto") -> float:
        """Calcula la distancia desde este punto hasta otro."""
        return hypot(self.x - p.x, self.y - p.y)

    @staticmethod
    def distancia_entre_puntos(a: Punto, b: Punto) -> float:
        """Calcula la distancia desde el punto a hasta el punto b"""
        return hypot(a.x - b.x, a.y - b.y)

    def desplazar(self, en_x, en_y):
        self.__x += en_x
        self.__y += en_y

    def __repr__(self):
        return f"Punto({self.x},{self.y})"

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __hash__(self):
        return hash(sqrt(self.x + self.y))


def main():
    """main"""
    p1 = Punto(1, 1)
    p2 = Punto(1, 1)
    conjupuntos = set()
    conjupuntos.add(p1)
    conjupuntos.add(p2)

    print(conjupuntos)


if __name__ == "__main__":
    main()
