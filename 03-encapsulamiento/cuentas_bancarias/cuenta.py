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

    def depositar(self, monto):
        """Deposita en monto en la cuenta si es un valor positivo"""
        if monto > 0:
            self.__saldo += monto
        else:
            print("El monto a depositar debe ser positivo")

    def extraer(self, monto):
        """Retira dinero si hay suficiente saldo"""
        if 0 <= monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("No hay saldo suficiente o monto inválido")


def main():
    pass


if __name__ == "__main__":
    main()
