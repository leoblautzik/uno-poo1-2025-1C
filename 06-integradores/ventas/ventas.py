from io import open


class CantidadInvalida(Exception):
    pass


class Ventas:
    def __init__(self):
        self.ventas_por_producto = {}

    def leer_ventas(self, archivo_entrada):
        with open(archivo_entrada, "r", encoding="UTF-8") as ventas:
            for linea in ventas:
                datos = linea.split(" ")
                cod_prod = datos[0]
                try:
                    cant = int(datos[1])
                    if cant <= 0 or cant > 1000:
                        raise CantidadInvalida(Exception)
                except ValueError:
                    print("Uno de los datos leidos no es un numero")
                    cant = 0
                except CantidadInvalida:
                    print("Una cantidad leida es inválida")
                    cant = 0
                acum = self.ventas_por_producto.setdefault(cod_prod, 0)
                acum += cant
                self.ventas_por_producto[cod_prod] = acum

    def escribir_ventas_por_producto(self, salida):
        with open(salida, "w", encoding="UTF-8") as vpp:
            for cod_pro, total in self.ventas_por_producto.items():
                vpp.write(f"{cod_pro} {total} \n")


def main():
    vpp = Ventas()
    vpp.leer_ventas("ventas.txt")
    vpp.escribir_ventas_por_producto("ventas_por_producto.txt")


if __name__ == "__main__":
    main()
