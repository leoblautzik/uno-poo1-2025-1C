"""Clase Unidad"""

from __future__ import annotations

from abc import ABCMeta, abstractmethod


class Unidad(metaclass=ABCMeta):
    """Clase abstracta unidad"""

    def __init__(self, salud, danio, posicion):
        self.__salud = salud
        self.__danio = danio
        self.__posicion = posicion

    @property
    def posicion(self):
        return self.__posicion

    @property
    def danio(self):
        return self.__danio

    @property
    def salud(self):
        return self.__salud

    @abstractmethod
    def atacar(self, enemigo: Unidad):
        pass

    def recibir_danio(self, danio):
        self.__salud -= danio

    def esta_muerto(self) -> bool:
        return self.__salud <= 0

    def distancia(self, enemigo: Unidad):
        return abs(self.__posicion - enemigo.posicion)
