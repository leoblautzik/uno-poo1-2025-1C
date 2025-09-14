from abc import ABC, abstractmethod


class Unidad(ABC):
    def __init__(self, salud, posicion):
        self.salud = salud
        self.posicion = posicion

    @abstractmethod
    def puede_atacar(self, objetivo) -> bool:
        pass

    @abstractmethod
    def atacar(self, objetivo):
        pass

    def recibir_ataque(self, atacante):
        # Reducir salud
        pass

    def esta_viva(self):
        return self.salud > 0


class Soldado(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=200, posicion=posicion)
        self.energia = 100

    def puede_atacar(self, objetivo):
        # Ejemplo: distancia == 1 y energía suficiente
        pass

    def atacar(self, objetivo):
        pass

    def recibir_agua(self):
        pass


class Arquero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=50, posicion=posicion)
        self.flechas = 20

    def puede_atacar(self, objetivo):
        # Ejemplo: 2 <= distancia <= 5 y flechas > 0
        pass

    def atacar(self, objetivo):
        pass

    def recibir_flechas(self, cantidad=6):
        pass


class Lancero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=150, posicion=posicion)

    def puede_atacar(self, objetivo):
        # Ejemplo: 1 <= distancia <= 3
        pass

    def atacar(self, objetivo):
        pass


class Caballero(Unidad):
    def __init__(self, posicion):
        super().__init__(salud=200, posicion=posicion)
        self.ataques_realizados = 0
        self.caballo_rebelde = False

    def puede_atacar(self, objetivo):
        # Ejemplo: 1 <= distancia <= 2 y caballo no rebelde
        pass

    def atacar(self, objetivo):
        pass

    def recibir_agua(self):
        pass
