"""

    /**
     * post: la instancia queda asignada al titular indicado y con saldo igual a 0.
     */
    public CajaDeAhorro(String titularDeLaCuenta) { }

    /**
     * post: devuelve el nombre del titular de la Caja de Ahorro.
     */
    public String obtenerTitular() { }

    /**
     * post: devuelve el saldo de la Caja de Ahorro.
     */
    public double consultarSaldo() { }

    /**
     * pre : monto es un valor mayor a 0.
     * post: aumenta el saldo de la Caja de Ahorro según el monto depositado.
     */
    public void depositar(double monto) { }

    /**
     * pre : monto es mayor a 0 y menor o igual que el saldo de la Caja de Ahorro.
     * post: disminuye el saldo de la Caja de Ahorro según el monto extraído.
     */
    public void extraer(double monto) { }
}
"""


class CajaDeAhorro:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("Monto invalido")
        self.__saldo += monto

    def extraer(self, monto):
        if monto <= 0:
            raise ValueError("Monto invalido")
        if monto > self.saldo:
            print("Saldo insuficiente")
        self.__saldo -= monto

    def __repr__(self):
        return f"Titular: {self.titular}, Saldo = {self.saldo}"


class Banco:
    def __init__(self, nombre) -> None:
        self.__cuentas: list[CajaDeAhorro] = []
        self.nombre = nombre

    def agregar_cuentas(self, c):
        self.__cuentas.append(c)

    def listar_cuentas(self):
        for cc in self.__cuentas:
            print(cc)

    def cuanta_plata(self):
        total = 0.0
        for cc in self.__cuentas:
            total += cc.saldo
        return total


def main():
    cl = CajaDeAhorro("Leo")
    cl.depositar(10000)
    cl.extraer(1000)
    cm = CajaDeAhorro("Mar")
    cm.depositar(100000)
    cz = CajaDeAhorro("Liz")
    cz.depositar(100)

    hcbc = Banco("HCBC")
    hcbc.agregar_cuentas(cl)
    hcbc.agregar_cuentas(cm)
    hcbc.agregar_cuentas(cz)
    hcbc.listar_cuentas()
    print("Total de saldos", hcbc.cuanta_plata())


if __name__ == "__main__":
    main()
