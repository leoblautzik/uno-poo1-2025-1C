from abc import ABCMeta, abstractmethod


class Deportista(metaclass=ABCMeta):
    __cuota_base = 100

    def __init__(self, dias):
        self.__socio = 0
        self.__dias = dias

    @property
    def socio(self):
        return self.__socio

    def set_numero_socio(self, numero):
        self.__socio = numero

    @property
    def dias(self):
        return self.__dias

    @classmethod
    def set_cuota_base(cls, cb):
        cls.__cuota_base = cb

    @classmethod
    def get_cuota_base(cls) -> float:
        return cls.__cuota_base

    @abstractmethod
    def get_cuota_mensual(self) -> float:
        pass

    def __str__(self):
        return (
            f"socio n°: {self.__socio}, Cuota mensual: {self.get_cuota_mensual():.2f}"
        )

    def __lt__(self, other):
        return self.socio < other.socio


class Tenista(Deportista):
    def get_cuota_mensual(self) -> float:
        return super().get_cuota_base() * (1 + super().dias * 0.05)


class Futbolista(Deportista):
    def get_cuota_mensual(self) -> float:
        return super().get_cuota_base() * (1 + super().dias * 0.1)


def main():
    pass


if __name__ == "__main__":
    main()
