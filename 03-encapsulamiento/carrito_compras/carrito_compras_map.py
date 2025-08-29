from producto import Producto


class CarritoCompras:
    def __init__(self):
        self.__productos = {}

    def agregar_producto(self, p: Producto, cantidad: int):
        if p.stock < cantidad:
            raise ValueError("Stock insuficiente")
        self.__productos[p] = cantidad

    def cotizar_carrito(self) -> float:
        total = 0.0
        for p, c in self.__productos.items():
            total += p.precio * c

        return total

    def comprar_carrito(self):
        for p, c in self.__productos.items():
            p.descontar_stock(c)

        # Vaciamos el carrito
        self.__productos = {}

    def __repr__(self):
        s = ""
        for p, c in self.__productos.items():
            s += f"{p.__repr__()}  Cantidad: {c}" + "\n"
        return s


def main():
    mate = Producto("Matecito", 23000, 10)
    bombilla = Producto("Bombilla alpaca", 3467.89, 3)

    mi_carrito = CarritoCompras()
    mi_carrito.agregar_producto(mate, 2)
    mi_carrito.agregar_producto(bombilla, 3)
    print("Mi carrito cuesta: ", mi_carrito.cotizar_carrito())
    print(mi_carrito)
    mi_carrito.comprar_carrito()
    print("productos con el stock actualizado")
    print(mate)
    print(bombilla)


if __name__ == "__main__":
    main()
