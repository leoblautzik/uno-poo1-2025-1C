"""Archivo de entrada: empleados.csv con nombre, sector y salario de cada empleado.

Ana, Ventas, 5000
Luis, IT, 6000
Juan, Ventas, 5500
Marta, IT, 6200

Implementar la class GestionEmpleados que guarde en una lista todos los empleados leídos del archivo.
Debe proveer un metodo que devuelve un diccionario donde la key sea el sector, y el value asociado, una lista con los empleados de ese sector.
Debe proveer un metodo que devuelva el sector que pague mayores sueldos en total.
Nota: Se debe implementar la class Empleado
"""


class Empleado:
    def __init__(self, nombre, sector, salario):
        self.nombre = nombre
        self.sector = sector
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} {self.sector} {self.salario}"


class GestionEmpleados:
    def __init__(self):
        self.empleados = []

    def leer_empleados(self, archivo):
        with open(archivo, "r", encoding="UTF-8") as archi:
            for linea in archi:
                datos = linea.split(",")
                empleado = Empleado(datos[0], datos[1], float(datos[2]))
                self.empleados.append(empleado)

    def empleados_por_sector(self):
        eps = {}
        for e in self.empleados:
            lista = eps.get(e.sector, [])
            lista.append(e)
            # eps.update({e.sector : lista})
            eps[e.sector] = lista

        return eps


def main():
    print(Empleado("pepe", "s1", 100))
    ge = GestionEmpleados()
    ge.leer_empleados("empleados.csv")
    print(ge.empleados)
    eps = ge.empleados_por_sector()
    print(eps)


if __name__ == "__main__":
    main()
