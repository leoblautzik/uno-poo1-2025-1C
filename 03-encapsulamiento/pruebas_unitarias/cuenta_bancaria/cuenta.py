# cuenta.py
class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, monto) -> None:
        self.__saldo += monto

    def retirar(self, monto) -> bool:
        if monto <= self.__saldo:
            self.__saldo -= monto
            return True
        return False

    def get_saldo(self):
        return self.__saldo


def main():
    pass


if __name__ == "__main__":
    main()
