import math
from abc import ABCMeta


class Figura(metaclass=ABCMeta):
    def __init__(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __str__(self):
        return f"{type(self).__name__}, Area: {self.get_area()}"


class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base * altura)


class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)


class Elipse(Figura):
    def __init__(self, radio_mayor, radio_menor):
        super().__init__(math.pi * radio_mayor + radio_menor)


class Circulo(Elipse):
    def __init__(self, radio):
        super().__init__(radio, radio)


def main():
    figuras = [Circulo(2), Rectangulo(2, 3), Cuadrado(4), Elipse(3, 5)]
    print(f for f in sorted(figuras, reverse=True))


if __name__ == "__main__":
    main()
