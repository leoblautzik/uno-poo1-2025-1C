from __future__ import annotations
from abc import ABC, abstractmethod


class Cuenta(ABC):
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0.00

    def get_titular(self):
        return self.__titular

    def consultar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if not self.es_monto_valido(monto):
            raise ValueError("Monto inválido")
        self.__saldo += monto

    def extraer(self, monto):
        if self.tiene_disponible(monto):
            self.__saldo -= monto

    @abstractmethod
    def dinero_disponible(self):
        pass

    def tiene_disponible(self, monto):
        return self.dinero_disponible() >= monto

    def transferir(self, otra: Cuenta, monto):
        if self.tiene_disponible(monto):
            self.extraer(monto)
            otra.depositar(monto)

    def es_monto_valido(self, monto: float) -> bool:
        return monto > 0


def main():
    pass


if __name__ == "__main__":
    main()
