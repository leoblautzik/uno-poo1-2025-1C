# Python - Sistema de Empleados


class Empleado:
    def __init__(self, nombre, salario_base, dni):
        self.__nombre = nombre
        self.set_salario_base(salario_base)
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, sb):
        if sb <= 0:
            raise ValueError("Valor incorrecto")
        self.__salario_base = sb

    def calcular_bonificacion(self):
        return self.__salario_base * 0.05

    def calcular_salario(self):
        return self.get_salario_base() + self.calcular_bonificacion()

    def __str__(self):
        return f"{self.__nombre}, {self.__dni}"


class Gerente(Empleado):
    def calcular_bonificacion(self):
        return super().get_salario_base() * 0.10


class Desarrollador(Empleado):
    def calcular_bonificacion(self):
        return super().get_salario_base() * 0.07


class Empresa:
    @classmethod
    def mostrar_bonificaciones(cls, empleados: list[Empleado]):
        for empleado in empleados:
            print(
                f"{empleado} -> Bonificación: ${empleado.calcular_bonificacion():.2f}"
            )

    @classmethod
    def imprimir_salarios(cls, empleados: list[Empleado]):
        resultados = []
        for empleado in empleados:
            resultados.append(
                (
                    "Nombre:",
                    empleado.get_nombre(),
                    "Salario",
                    empleado.calcular_salario(),
                )
            )
        return resultados


# Ejemplo de uso
def main():
    empleados = [
        Gerente("Ana Torres", 50000, "12345678"),
        Desarrollador("Luis Gómez", 100000, "23456789"),
        Empleado("Marta Ruiz", 70000, "34567890"),
    ]
    Empresa.mostrar_bonificaciones(empleados)
    print(Empresa.imprimir_salarios(empleados))


if __name__ == "__main__":
    main()
