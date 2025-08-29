from producto import Producto


class CarritoCompras:
    def __init__(self):
        self.__productos: list[Producto] = []
        self.__cantidades: list[int] = []

    def agregar_producto(self, p: Producto, cantidad: int):
        if p.stock < cantidad:
            raise ValueError("Stock insuficiente")
        self.__productos.append(p)
        self.__cantidades.append(cantidad)

    def cotizar_carrito(self) -> float:
        total = 0.0
        for i in range(len(self.__cantidades)):
            total += self.__productos[i].precio * self.__cantidades[i]
        return total

    def comprar_carrito(self):
        for i in range(len(self.__productos)):
            self.__productos[i].descontar_stock(self.__cantidades[i])

    def __repr__(self):
        s = ""
        for p, c in zip(self.__productos, self.__cantidades):
            s += p.__repr__() + " Cantidad: " + str(c) + "\n"
        return s


def main():
    mate = Producto("Matecito", 23000, 10)
    bombilla = Producto("Bombilla alpaca", 3467.89, 3)

    mi_carrito = CarritoCompras()
    mi_carrito.agregar_producto(mate, 2)
    mi_carrito.agregar_producto(bombilla, 3)
    print(mi_carrito.cotizar_carrito())
    print(mi_carrito)
    mi_carrito.comprar_carrito()
    print(mi_carrito)


if __name__ == "__main__":
    main()
