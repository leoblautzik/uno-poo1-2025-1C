class Empleado:
    def __init__(self, nombre, sector, salario: float) -> None:
        self.nombre = nombre
        self.sector = sector
        self.salario: float = salario


class GestionEmpleados:
    def __init__(self, file) -> None:
        self.empleados: list[Empleado] = []
        self.cargar_empleados(file)

    def cargar_empleados(self, file):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
