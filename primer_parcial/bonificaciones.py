# Python - Sistema de Empleados


class Empleado:
    def __init__(self, nombre, salario_base, dni):
        self._nombre = nombre
        self._salario_base = salario_base
        self._dni = dni

    def get_nombre(self):
        return self._nombre

    def get_salario(self):
        return self._salario_base

    def calcular_bonificacion(self):
        return self._salario_base * 0.05


class Gerente(Empleado):
    def calcular_bonificacion(self):
        return self._salario_base * 0.10


class Desarrollador(Empleado):
    def calcular_bonificacion(self):
        return self._salario_base * 0.07


class Empresa:
    @staticmethod
    def mostrar_bonificaciones(empleados):
        for emp in empleados:
            print(
                f"Nombre: {emp.get_nombre()} - Bonificación: ${emp.calcular_bonificacion():.2f}"
            )


# Ejemplo de uso
def main():
    empleados = [
        Gerente("Ana Torres", 50000, "12345678"),
        Desarrollador("Luis Gómez", 100000, "23456789"),
        Empleado("Marta Ruiz", 70000, "34567890"),
    ]
    Empresa.mostrar_bonificaciones(empleados)


if __name__ == "__main__":
    main()
