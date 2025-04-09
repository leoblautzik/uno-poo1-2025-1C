"""Modelamos una Cuenta Corriente definiendo un descubierto al momento de la apertura"""

from cuenta import Cuenta


class CuentaCorriente:
    """Modelamos una Cuenta Corriente definiendo un descubierto al momento de la apertura
    La CuentaCorriente contiene una Cuenta"""

    def __init__(self, titular, descubierto):
        self.__cuenta = Cuenta(titular, 0)
        self.__descubierto = descubierto
        self.__descubierto_usado = 0

    def consultar_saldo(self):
        """Devulelve el saldo de la cuenta"""
        return self.__cuenta.consultar_saldo() - self.__descubierto_usado

    def obtener_titular(self):
        """Devulelve el titular de la cuenta"""
        return self.obtener_titular()

    def depositar(self, monto):
        """Deposita en monto en la cuenta si es un valor positivo"""
        if monto > self.__descubierto_usado:
            self.__cuenta.depositar(monto - self.__descubierto_usado)
            self.__descubierto_usado = 0
        else:
            self.__descubierto_usado -= monto

    def hay_dinero_suficiente(self, monto):
        """Devuelve True si hay disponible para realizar la operacion"""
        return self.disponible() >= monto

    def disponible(self):
        """Devuelve el dinero que hay disponible"""
        return self.__cuenta.consultar_saldo() + (
            self.__descubierto - self.__descubierto_usado
        )

    def extraer(self, monto) -> float:
        """Permite extraer dinero hasta el limite del descubierto"""
        platita = 0.0
        if not self.hay_dinero_suficiente(monto):
            print("No hay dinero disponible")
        elif monto <= self.__cuenta.consultar_saldo():
            platita = self.__cuenta.extraer(monto)
        elif monto <= self.disponible():
            self.__descubierto_usado += monto - self.__cuenta.consultar_saldo()
            platita = self.__cuenta.extraer(self.__cuenta.consultar_saldo())
        return platita

    def transferir(self, destino, monto):
        destino.depositar(self.extraer(monto))


def main():
    """Demo"""
    cc = CuentaCorriente("Pepe", 1000)
    cc.depositar(500)
    print(cc.consultar_saldo())
    cc.extraer(1500.50)
    print(cc.consultar_saldo())
    cc.depositar(200)
    print(cc.consultar_saldo())
    cc.depositar(300)
    print(cc.consultar_saldo())


if __name__ == "__main__":
    main()
