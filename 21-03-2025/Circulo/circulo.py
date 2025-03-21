import math


class Circulo:
    def __init__(self, radio, xc, yc, color):
        self.__radio = radio
        self.__xc = xc
        self.__yc = yc
        self.__color = color

    def area(self):
        return math.pi * pow(self.radio, 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def diametro(self):
        return 2 * self.radio

    def __repr__(self):
        rep = f"Soy un circulo de radio {self.radio} y color {self.color}"
        return rep


c1 = Circulo(2, 1, 1, "rojo")
c2 = Circulo(4, 2, -2, "azul")
print(c1)
print(c2)
print("radio de c1: ", c1.radio)
print("diametro de c1: ", c1.diametro())
print(c2.perimetro())
print(c1.color)
print(c1.area())
print(c2.area())
