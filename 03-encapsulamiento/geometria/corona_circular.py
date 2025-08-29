"""Implementar una clase que modele una corona circular
utilizando la clase Circulo desarrollada previamente.
Se desea manipular (obtener y/o cambiar):
radio interior
radio exterior
perímetro interior
perímetro exterior
área
queremos poder desplazar la corona a otro punto del plano
"""

from circulo import Circulo
from color import Color
from punto import Punto


class CoronaCircular:
    """Modela una corona circular a partir de la clase Circulo
    con un Punto como centro"""

    def __init__(self, ri, re, xc, yc, color):
        self.__ci = Circulo(ri, xc, yc, color)
        self.__ce = Circulo(re, xc, yc, color)

    @property
    def centro(self) -> Punto:
        """Devuelve un objeto Punto que es el centro de la CC"""
        return self.__ci.centro

    @property
    def color(self) -> Color:
        """Devuelce el Color de la CC que es un enumerado de Color"""
        return self.__ce.color

    def perimetro_interior(self):
        """Devuelve el perimetro interior"""
        return self.__ci.perimetro()

    def perimetro_exterior(self) -> float:
        """Devuelve el perimetro exterior"""
        return self.__ce.perimetro()

    def area(self):
        """Devuelve el area de la CC"""
        return self.__ce.area() - self.__ci.area()

    def desplazar(self, en_x, en_y):
        """Desplaza el centro de la CC segun los parametros en_x y en_y"""
        self.__ce.desplazar(en_x, en_y)
        self.__ci.desplazar(en_x, en_y)


def main():
    """funcion main"""
    c = CoronaCircular(2, 4, 1, 1, "rojo")
    print(c.area())
    print(c.perimetro_interior())
    print(c.perimetro_exterior())
    print(c.centro)
    c.desplazar(2, 3)
    print(c.centro)


if __name__ == "__main__":
    main()
