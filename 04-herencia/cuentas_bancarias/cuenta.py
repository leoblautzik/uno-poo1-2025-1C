"""Un banco contiene las Cuentas de sus clientes.
Las cuentas de ahorro no pueden tener números rojos.
Las cuentas corrientes pueden girar en descubierto hasta  un monto
que se define al momento de su creación.
Define Cuenta de forma que no pueda instanciarse.
De toda Cuenta se debe poder ingresar y retirar dinero,
preguntar por el saldo, por el DNI del titular y debe tener un método toString()
que devuelva al menos el saldo y el DNI del titular.
Implementar las clases CuentaCorriente y CuentaDeAhorro como una especialización de Cuenta.
De una cuenta se debe poder transferir dinero a otra cuenta (si tiene dinero disponible).
Implementa la clase Banco que contiene una colección de Cuentas, incluye los métodos:
public Cuenta abrirCuentaCorriente(int dni, double descubierto){}
public Cuenta abrirCajaDeAhorro(int dni){}
public double totalSaldoEnDescubierto(){}
// devuelve la suma de los saldos de todas las cuentas
corrientes que están en descubierto,
public void listarCuentas(){}
// que muestra los datos de todas las cuentas del banco,
ordenado por saldo de manera ascendente.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Cuenta(ABC):
    """Define Cuenta de forma que no pueda instanciarse.
    Clase abstracta en python
    """

    def __init__(self, titular):
        self.__saldo = 0.00
        self.__titular = titular

    def obtener_titular(self):
        """devuelve el dni del titular de la cuenta"""

        return self.__titular

    def consultar_saldo(self) -> float:
        """devuelve el saldo de la cuenta"""

        return self.__saldo

    # def set_saldo(self, s):
    #     """Establece el saldo en s"""
    #     self.__saldo = s

    @abstractmethod
    def hay_dinero_suficiente(self, monto) -> bool:
        """Devuelve true o false, segun alcance el saldo para
        hacer la operacion"""

    @abstractmethod
    def get_dinero_disponible(self) -> float:
        """Devuelve el total del dinero del que dispone el titular de la cuenta"""

    def extraer(self, monto) -> float:
        """de todas las cuentas se debe poder extraer dinero,
        si hay dinero suficiente. No tiene el mismo comportamiento
        para cuentas de ahorro que para cuentas corrientes"""

        platita = 0
        if self.hay_dinero_suficiente(monto):
            self.__saldo -= monto
            platita = monto

        return platita

    def depositar(self, monto):
        """Incrementa el saldo en el monto que se pasa por parametro"""

        if monto <= 0:
            raise ValueError("Monto incorrecto")
        self.__saldo += monto

    def transferir(self, destino: Cuenta, monto: float):
        """Transfiere el monto desde la cuenta self a la cuenta destino"""
        if self.hay_dinero_suficiente(monto):
            self.extraer(monto)
            destino.depositar(monto)

    def __repr__(self) -> str:
        return "Titular: " + str(self.__titular) + ", Saldo: " + str(self.__saldo)
