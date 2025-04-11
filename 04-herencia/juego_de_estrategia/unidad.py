"""Clase Unidad"""

from abc import ABCMeta, abstractmethod


class Unidad(metaclass=ABCMeta):
    def __init__(self, salud, danio, posicion):
        self.salud = salud
        self.danio = danio
        self.posicion = posicion

    @abstractmethod
    def atacar(self, enemigo):
        pass

    def recibir_danio(self, danio):
        self.salud -= danio

    def esta_muerto(self) -> bool:
        return self.salud <= 0

    def distancia(self, enemigo):
        return abs(self.posicion - enemigo.posicion)
