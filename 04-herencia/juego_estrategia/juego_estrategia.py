from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
import math


class Aguatero(metaclass=ABCMeta):
    @abstractmethod
    def recibir_agua(self):
        pass


class Unidad(ABC):
    def __init__(self, salud, danio, posicion):
        self.salud = salud
        self.danio = danio
        self.posicion = posicion

    @abstractmethod
    def puede_atacar(self, objetivo: Unidad) -> bool:
        pass

    @abstractmethod
    def atacar(self, objetivo):
        pass

    def recibir_ataque(self, atacante: Unidad):
        self.salud -= atacante.danio

    def esta_viva(self):
        return self.salud > 0


class Soldado(Unidad, Aguatero):
    def __init__(self, posicion):
        super().__init__(salud=200, danio=10, posicion=posicion)
        self.energia = 100

    def puede_atacar(self, objetivo: Unidad) -> bool:
        # Ejemplo: distancia == 0 y energía suficiente,
        # no esta muerto, y el oponente tampoco
        return (
            self.posicion - objetivo.posicion == 0
            and self.energia >= 10
            and self.esta_viva()
            and objetivo.esta_viva()
        )

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            objetivo.recibir_ataque(self)
            self.energia -= 10

    def recibir_agua(self):
        self.energia = 100


class Arquero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=50, danio=5, posicion=posicion)
        self.flechas = 20

    def puede_atacar(self, objetivo: Unidad) -> bool:
        # Ejemplo: 2 <= distancia <= 5 y flechas > 0
        distancia = math.fabs(self.posicion - objetivo.posicion)
        return (
            2 <= distancia <= 5
            and self.flechas > 0
            and self.esta_viva()
            and objetivo.esta_viva()
        )

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            self.flechas -= 1
            objetivo.recibir_ataque(self)

    def recibir_flechas(self, cantidad=6):
        self.flechas += cantidad


class Lancero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=150, danio=25, posicion=posicion)

    def puede_atacar(self, objetivo: Unidad) -> bool:
        # Ejemplo: 1 <= distancia <= 3
        distancia = self.posicion - objetivo.posicion
        return (
            distancia >= 1
            and distancia <= 3
            and self.esta_viva()
            and objetivo.esta_viva()
        )

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            objetivo.recibir_ataque(self)


class Caballero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=200, danio=50, posicion=posicion)
        self.caballo = Caballo()

    def puede_atacar(self, objetivo: Unidad) -> bool:
        distancia = abs(self.posicion - objetivo.posicion)
        return 1 <= distancia <= 2 and not self.caballo.esta_rebelde()

    def atacar(self, objetivo: Unidad):
        if self.puede_atacar(objetivo):
            self.caballo.contar_ataques()
            objetivo.recibir_ataque(self)

    def recibir_agua(self):
        self.caballo.recibir_agua()


class Caballo(Aguatero):
    def __init__(self):
        self.__ataques_realizados = 0
        # self.__rebelde = False

    def recibir_agua(self):
        self.__ataques_realizados = 0

    def contar_ataques(self):
        if not self.esta_rebelde():
            self.__ataques_realizados += 1

    def esta_rebelde(self):
        return self.__ataques_realizados >= 3


class Escudo(Unidad):
    def __init__(self, unidad: Unidad):
        self.unidad: Unidad = unidad
        self.posicion = unidad.posicion

    def atacar(self, objetivo: Unidad):
        self.unidad.atacar(objetivo)

    def puede_atacar(self, objetivo: Unidad) -> bool:
        return self.unidad.puede_atacar(objetivo)

    def recibir_ataque(self, atacante):
        danio_reducido = atacante.danio * 0.4
        self.unidad.salud -= danio_reducido

    def esta_viva(self):
        return self.unidad.esta_viva()
