"""
Archivo de entrada: empleados.csv
con nombre, sector y salario de cada empleado.

Ana, Ventas, 5000
Luis, IT, 6000
Juan, Ventas, 5500
Marta, IT, 6200

Implementar la class GestionEmpleados que guarde en una lista
todos los empleados leídos del archivo.
Debe proveer un metodo que devuelve un diccionario donde la key sea el sector,
y el value asociado, una lista con los empleados de ese sector.
Debe proveer un metodo que devuelva el sector que pague mayores sueldos en total.
Nota: Se debe implementar la class Empleado
"""


class Empleado:
    def __init__(self, nombre, sector, salario):
        self.nombre = nombre
        self.sector = sector
        self.salario = salario


class GestionEmpleados:
    def __init__(self):
        self.empleados: list[Empleado] = []

    def leer_empleados(self, archivo_e):
        with open(archivo_e, "r") as emp:
            for cada_empleado in emp:
                datos = cada_empleado.strip().split(",")
                self.empleados.append(Empleado(datos[0], datos[1], float(datos[2])))
        emp.close()

    def emp_del_sector(self) -> dict[str, list[Empleado]]:
        sp: dict[str, list[Empleado]] = {}

        for e in self.empleados:
            # if e.sector not in sp.keys():
            #     le = []
            # else:
            #     le = sp[e.sector]

            le = sp.setdefault(e.sector, [])
            le.append(e.nombre)
            sp[e.sector] = le

        return sp

    def sector_mayor_salario_total(self) -> tuple[str, float]:
        ss: dict[str, float] = {}

        for e in self.empleados:
            if e.sector not in ss.keys():
                salario = 0
            else:
                salario = ss[e.sector]
            salario += e.salario
            ss[e.sector] = salario

        return max(ss.items(), key=lambda item: item[1])


def main():
    ge = GestionEmpleados()
    ge.leer_empleados("empleados.csv")

    print(ge.emp_del_sector())
    print(ge.sector_mayor_salario_total())


if __name__ == "__main__":
    main()
