"""
Gestion Vemtas Informática
"""


class Venta:
    """Modela las ventas del día tomadas del archivo de ventas"""

    def __init__(
        self, codigo, descripcion, categoria, precio_unitario, cantidad, vendedor
    ):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__categoria = categoria
        self.__precio_unitario = float(precio_unitario)
        self.__cantidad = int(cantidad)
        self.__vendedor = str(vendedor)

    @property
    def vendedor(self):
        return self.__vendedor

    @property
    def categoria(self):
        return self.__categoria

    @property
    def codigo(self):
        """The codigo property."""
        return self.__codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def precio_unitario(self) -> float:
        return self.__precio_unitario

    @property
    def cantidad(self):
        """The cantidad property."""
        return self.__cantidad

    def monto_total(self):
        return self.__precio_unitario * self.__cantidad

    def __repr__(self):
        return f"{self.__codigo} - {self.__descripcion} - ${self.monto_total()}"


class Producto:
    """
    Class Producto
    """

    def __init__(self, codigo, descripcion, precio: float):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio

    def __hash__(self):
        return hash(self.codigo)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Producto):
            return False
        else:
            return (
                self.codigo == other.codigo
                and self.descripcion == other.descripcion
                and self.precio_unitario == other.precio_unitario
            )

    def __str__(self):
        return f"{self.codigo} - {self.descripcion} $ {self.precio_unitario}"


class GestionVentas:
    def __init__(self):
        self.__ventas: list[Venta] = []
        self.__productos: list[Producto] = []

    def leer_ventas(self, file_ventas):
        with open(file_ventas, "r", encoding="UTF-8") as ventas:
            for cada_linea in ventas:
                datos = cada_linea.strip().split(",")
                self.__ventas.append(
                    Venta(datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])
                )

    def obtener_total_ventas(self) -> float:
        total = 0.00
        for venta in self.__ventas:
            total += venta.monto_total()
        return total

    def ventas_vendedor(self) -> dict[str, float]:
        vv: dict[str, float] = {}
        for venta in self.__ventas:
            if venta.vendedor not in vv.keys():
                monto_actualizado = venta.monto_total()
            else:
                monto_actualizado = vv[venta.vendedor] + venta.monto_total()
            vv[venta.vendedor] = monto_actualizado

        return vv

    def producto_mas_vendido(self) -> tuple[str, int]:
        pc: dict[str, int] = {}
        for venta in self.__ventas:
            if venta.codigo not in pc.keys():
                cantidad_vendida = venta.cantidad
            else:
                cantidad_vendida = pc[venta.codigo] + venta.cantidad
            pc[venta.codigo] = cantidad_vendida
        produ_max, cant_max = max(pc.items(), key=lambda item: item[1])

        return self.obtener_descripcion(produ_max), cant_max

    def vendedor_del_dia(self) -> tuple[str, float]:
        """Devuelve el vendedor que hizo el mayor volumen de ventas en $"""
        vv = self.ventas_vendedor()
        vendedor_d, venta_max = max(vv.items(), key=lambda item: item[1])
        return vendedor_d, venta_max

    def obtener_descripcion(self, codigo) -> str:
        for v in self.__ventas:
            if v.codigo == codigo:
                return v.descripcion
        return ""

    def obtener_precio_unitario(self, codigo):
        for v in self.__ventas:
            if v.codigo == codigo:
                return v.precio_unitario
        return None

    def obtener_categorias(self) -> list[str]:
        categorias = []
        for v in self.__ventas:
            if v.categoria not in categorias:
                categorias.append(v.categoria)
        return categorias

    def metodo(self):
        return self.obtener_precio_unitario("")

    def obtener_productos(self) -> list[Producto]:
        # productos: list[Producto] = []
        if len(self.__productos) == 0:
            for v in self.__ventas:
                p = Producto(v.codigo, v.descripcion, v.precio_unitario)
                if p not in self.__productos:
                    self.__productos.append(p)

        return self.__productos

    def resumen_ventas(self):
        with open("resumen_ventas.txt", "w", encoding="UTF-8") as output:
            output.write(f"Total de ventas: ${self.obtener_total_ventas():.2f} \n")
            d, c = self.producto_mas_vendido()
            output.write(f"Producto más vendido: {d} -> cantidad: {c} \n")
            v, p = self.vendedor_del_dia()
            output.write(f"Vendedor del día: {v} -> importe: ${p:.2f} \n")
            output.write("Totales por vendedor: \n")
            for v, p in self.ventas_vendedor().items():
                v += ":"
                output.write(f"\t- {v:15} ${p:.2f} \n")


def main():
    gv = GestionVentas()
    gv.leer_ventas("ventas.txt")
    gv.resumen_ventas()


if __name__ == "__main__":
    main()
