from abc import ABCMeta, abstractmethod


class Mascota(metaclass=ABCMeta):
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__vacunado = False

    @abstractmethod
    def emitir_somido(self):
        pass

    def vacunar(self):
        self.__vacunado = True

    def __str__(self):
        return f"Soy un {type(self).__name__}. \nMe llamo {self.__nombre}, tengo {self.__edad} años y hago {self.emitir_somido()} estoy vacunado? {self.__vacunado}"
