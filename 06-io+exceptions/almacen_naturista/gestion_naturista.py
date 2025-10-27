import csv


class StockInsuficienteException(Exception):
    pass


class Producto:
    """Cada producto tiene:
    código, descripción, precio unitario y stock disponible.
    """

    def __init__(self, codigo, descripcion, precio):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio = precio

    def __repr__(self) -> str:
        return f"{self.codigo}, {self.descripcion}, {self.precio}"

    def __eq__(self, otro) -> bool:
        return self.codigo == otro.codigo

    def __hash__(self) -> int:
        return hash(self.codigo)


class Venta:
    """producto vendido (por código), su descripción, el precio unitario y la cantidad vendida."""

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad


class GestorProductos:
    def __init__(self, csv_productos, csv_ventas):
        self.productos = []
        self.ventas = {}
        self.stock = {}
        self.__leer_productos(csv_productos)
        self.__leer_ventas(csv_ventas)

    def __leer_productos(self, csv_productos):
        with open(
            csv_productos,
            newline="",
        ) as a_prod:
            lector = csv.reader(a_prod)
            for codigo, descripcion, precio, stock in lector:
                try:
                    precio = float(precio)
                    stock = int(stock)
                    prod = Producto(codigo, descripcion, precio)
                    self.productos.append(prod)
                    self.stock[prod] = stock
                except ValueError:
                    pass

    def __leer_ventas(self, csv_ventas):
        with open(csv_ventas, newline="") as a_ventas:
            lector = csv.reader(a_ventas)
            for codigo, descripcion, precio, cantidad in lector:
                try:
                    precio = float(precio)
                    cantidad = int(cantidad)
                    prod = Producto(codigo, descripcion, precio)
                    if cantidad > self.stock[prod]:
                        raise StockInsuficienteException
                    self.stock[prod] = self.stock[prod] - cantidad
                    # actualizo la cantidad vendida
                    cantidad_actual = self.ventas.setdefault(prod, 0)
                    self.ventas[prod] = cantidad + cantidad_actual
                except ValueError:
                    pass
                except StockInsuficienteException:
                    pass


def main():
    gp = GestorProductos("productos.csv", "ventas.csv")
    print("Stock")
    print(gp.stock)
    print("Ventas")
    print(gp.ventas)

    print("Stock")
    print(gp.stock)


if __name__ == "__main__":
    main()
