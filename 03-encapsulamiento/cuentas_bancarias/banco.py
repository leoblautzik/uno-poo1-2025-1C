from caja_ahorro import CajaAhorro
from cuenta_corriente import CuentaCorriente


class Banco:
    def __init__(self):
        self.__cajas_ahorro = []
        self.__cuentas_corrientes = []

    def abrir_caja_ahorro(self, titular):
        ca = CajaAhorro(titular)
        self.__cajas_ahorro.append(ca)

    def abrir_cuenta_corriente(self, titular, descubierto):
        cc = CuentaCorriente(titular, descubierto)
        self.__cuentas_corrientes.append(cc)

    def obtener_total_descubierto(self):
        tdcc = 0
        for cc in self.__cuentas_corrientes:
            tdcc += cc.consultar_saldo()
        return tdcc

    def extraer(self, titular, monto):
        for c in self.__cajas_ahorro:
            if c.obtener_titular() == titular:
                c.extraer(monto)
                break


def main():
    b = Banco()
    b.abrir_caja_ahorro("Leoblau")
    b.abrir_cuenta_corriente("Monica", 10000)
    print(b.obtener_total_descubierto())
    b.extraer("Monica", 5000)

    ca = CajaAhorro("Abc")
    ca.depositar(10000)
    cc = CuentaCorriente("Bcd", 3000)
    cc.depositar(4000)
    cc.transferir(ca, 1000)
    print(cc.consultar_saldo(), ca.consultar_saldo())
    ca.transferir(cc, 2000)
    print(cc.consultar_saldo(), ca.consultar_saldo())


if __name__ == "__main__":
    main()
