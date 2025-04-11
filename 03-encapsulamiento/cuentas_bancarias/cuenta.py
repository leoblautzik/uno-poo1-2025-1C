class Cuenta:
    """Modelamos una cuenta bancaria con sus operaciones basicas"""

    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial

    def consultar_saldo(self):
        """Devulelve el saldo de la cuenta"""
        return self.__saldo

    def obtener_titular(self):
        """Devulelve el titular de la cuenta"""
        return self.__titular

    def depositar(self, monto: float):
        """Deposita el monto en la cuenta si es un valor positivo"""
        if monto > 0.0:
            self.__saldo += monto
        else:
            print("El monto a depositar debe get_saldoser positivo")

    def extraer(self, monto: float) -> float:
        """Retira dinero si hay suficiente saldo"""
        platita = 0.0
        if self.hay_dinero_suficiente(monto):
            self.__saldo -= monto
            platita = monto
        else:
            print("No hay saldo suficiente o monto inválido")

        return platita

    def hay_dinero_suficiente(self, monto) -> bool:
        return 0 <= monto <= self.__saldo

    def transferir(self, destino, monto):
        destino.depositar(self.extraer(monto))


def main():
    pass


if __name__ == "__main__":
    main()
