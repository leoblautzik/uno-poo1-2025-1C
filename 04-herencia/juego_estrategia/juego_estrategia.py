from __future__ import annotations
from abc import ABC, abstractmethod
import math


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


class Soldado(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=200, danio=10, posicion=posicion)
        self.energia = 100

    def puede_atacar(self, objetivo: Unidad):
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

    def puede_atacar(self, objetivo: Unidad):
        # Ejemplo: 2 <= distancia <= 5 y flechas > 0
        distancia = math.fabs(self.posicion - objetivo.posicion)
        return (
            2 <= distancia <= 5
            and self.flechas > 0
            and self.esta_viva()
            and objetivo.esta_viva()
        )

    def atacar(self, objetivo):
        if self.puede_atacar(objetivo):
            self.flechas -= 1
            objetivo.recibir_danio(self)

    def recibir_flechas(self, cantidad=6):
        self.flechas += cantidad


class Lancero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=150, danio=25, posicion=posicion)

    def puede_atacar(self, objetivo: Unidad):
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
        self.ataques_realizados = 0
        self.caballo_rebelde = False

    def puede_atacar(self, objetivo):
        # Ejemplo: 1 <= distancia <= 2 y caballo no rebelde
        pass

    def atacar(self, objetivo):
        pass

    def recibir_agua(self):
        pass


class Escudo(Unidad):
    def __init__(self, unidad: Unidad):
        self.unidad = unidad
        self.posicion = unidad.posicion

    def atacar(self, objetivo: Unidad):
        self.unidad.atacar(objetivo)

    def puede_atacar(self, objetivo):
        self.unidad.puede_atacar(objetivo)

    def recibir_ataque(self, atacante):
        danio_reducido = atacante.danio * 0.4
        self.unidad.salud -= danio_reducido

    def esta_viva(self):
        return self.unidad.esta_viva()


rambo = Soldado(0)
conan = Lancero(1)
rambo_con_escudo = Escudo(Soldado(0))
conan.atacar(rambo)
conan.atacar(rambo_con_escudo)
print(rambo.salud)
print(rambo_con_escudo.unidad.salud)
rambo_con_escudo.atacar(conan)
