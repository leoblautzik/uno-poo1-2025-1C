"""Class Cuenta Corriente"""

from cuenta import Cuenta


class CuentaCorriente(Cuenta):
    """Class Cuenta Corriente
    Las cuentas corrientes pueden girar en descubierto hasta  un monto
    que se define al momento de su creación.
    """

    def __init__(self, dni, descubierto):
        super().__init__(dni)
        self.__descubierto = descubierto

    def get_descubierto(self):
        """Devuelve el descubierto definido en la cuenta"""
        return self.__descubierto

    def hay_dinero_suficiente(self, monto) -> bool:
        return super().consultar_saldo() + self.__descubierto >= monto

    def get_dinero_disponible(self) -> float:
        return super().consultar_saldo() + self.get_descubierto()

    def extraer(self, monto) -> float:
        if self.hay_dinero_suficiente(monto):
            if self.get_dinero_disponible() >= monto:
                super().extraer(monto)
        return monto

    def __str__(self) -> str:
        return super().__str__() + ", Descubierto: " + str(self.__descubierto)
