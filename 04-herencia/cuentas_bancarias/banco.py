"""Implementa la clase Banco que contiene una colección de Cuentas, incluye los métodos:
abrirCuentaCorriente(dni, descubierto)
abrirCajaDeAhorro(int dni)
totalSaldoEnDescubierto() -> devuelve la suma de los saldos de todas las cuentas corrientes
que están en descubierto.
listarCuentas() -> que muestra los datos de todas las cuentas del banco,
ordenado por saldo de manera ascendente.
"""

from cuenta import Cuenta
from cuenta_ahorro import CajaDeAhorro
from cuenta_corriente import CuentaCorriente


class Banco:
    """Class Banco"""

    def __init__(self) -> None:
        self.__cuentas: list[Cuenta] = []

    def abrir_caja_ahorro(self, dni) -> CajaDeAhorro:
        """Crea una caja de ahorro y la agrega a la lista de cuentas"""
        return CajaDeAhorro(dni)

    def abrir_cuenta_corriente(self, dni, descubierto) -> CuentaCorriente:
        """dniCrea una cuenta corriente y la agrega a la lista de cuentas"""
        return CuentaCorriente(dni, descubierto)

    def agregar_cuenta(self, c: Cuenta):
        """Agrega la cuenta c a la lista de cuentas del banco"""
        self.__cuentas.append(c)

    def listar_cuentas(self):
        """Muestra por pantalla la lista de cuentas del banco"""
        for cuenta in self.__cuentas:
            print(cuenta)

    def listar_cuentas_en_descubierto(self):
        """Muestra por pantalla la lista de cuentas corrientes que estan
        en descubierto"""
        for c in self.__cuentas:
            if isinstance(c, CuentaCorriente):
                if c.consultar_saldo() < 0:
                    print(c)


def main():
    bco = Banco()
    cc1 = bco.abrir_cuenta_corriente(12345678, 10000)
    ca1 = bco.abrir_caja_ahorro(23456789)
    bco.agregar_cuenta(cc1)
    bco.agregar_cuenta(ca1)
    bco.listar_cuentas()
    cc1.depositar((50000))
    ca1.depositar(20000)
    ca1.reservar(5000)
    print("Listado de cuentas: ")
    bco.listar_cuentas()
    cc1.extraer(55000)
    print("Listado de cuentas en descubierto: ")
    bco.listar_cuentas_en_descubierto()


if __name__ == "__main__":
    main()
