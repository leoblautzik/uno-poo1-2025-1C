import math

from color import Color
from punto import Punto


class Circulo:
    def __init__(self, radio, xc, yc, color: Color):
        self.__radio = radio
        self.__centro = Punto(xc, yc)
        self.__color = color

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        if radio <= 0:
            raise ValueError("El radio debe ser >= 0")
        self.__radio = radio

    @property
    def centro(self):
        return self.__centro

    @property
    def color(self):
        return self.__color

    def area(self):
        return math.pi * pow(self.radio, 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def diametro(self):
        return 2 * self.radio

    def __repr__(self):
        return f"Soy un circulo de radio {self.radio} y color {self.__color.name}"

    def desplazar(self, en_x, en_y):
        self.centro.desplazar(en_x, en_y)


def main():
    c1 = Circulo(2, 1, 1, Color.ROJO)
    c2 = Circulo(4, 2, -2, Color.AZUL)
    print(c1)
    print(c2)
    print("radio de c1: ", c1.radio)
    print("diametro de c1: ", c1.diametro())
    print(c2.perimetro())
    print(c1.color)
    print(c1.area())
    print(c2.area())


if __name__ == "__main__":
    main()
