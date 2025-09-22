from __future__ import annotations
from abc import ABC
import math
from typing import final


class Figura(ABC):
    def __init__(self, area: float) -> None:
        self.__area: float = area

    @final
    def get_area(self) -> float:
        return self.__area

    def __lt__(self, otra: Figura) -> bool:
        return self.get_area() < otra.get_area()

    def __eq__(self, otra) -> bool:
        if isinstance(Figura, otra):
            return self.get_area() == otra.get_area()
        return False

    def __repr__(self) -> str:
        return ""


class Elipse(Figura):
    def __init__(self, radio_mayor, radio_menor):
        super().__init__(math.pi * radio_mayor * radio_menor)

    def __repr__(self) -> str:
        return f"Elipse: {self.get_area():.2f}"


class Circulo(Elipse):
    def __init__(self, radio):
        super().__init__(radio, radio)

    def __repr__(self):
        return f"Circulo: {self.get_area():.2F}"


class Rectangulo(Figura):
    def __init__(self, base, altura) -> None:
        super().__init__(base * altura)

    def __repr__(self):
        return f"Rectangulo: {self.get_area():.2f}"


class Cuadrado(Rectangulo):
    def __init__(self, lado) -> None:
        super().__init__(lado, lado)

    def __repr__(self):
        return f"Cuadrado: {self.get_area():.2f}"


class Triangulo(Figura):
    def __init__(self, base, altura) -> None:
        super().__init__(base * altura / 2)

    def __repr__(self):
        return f"Triangulo de area: {self.get_area():.2f}"


def main():
    cuadradito = Cuadrado(5)
    elipsita = Elipse(3, 6)
    circulito = Circulo(5)
    rectangulito = Rectangulo(4, 9.00)
    triangulito = Triangulo(4.00, 9.00)

    figuras = [cuadradito, elipsita, circulito, rectangulito, triangulito]

    print(sorted(figuras))
    print(figuras)


if __name__ == "__main__":
    main()
