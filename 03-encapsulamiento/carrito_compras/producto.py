class Producto:
    # Atributos privados: __nombre __precio  __stock
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        self.__nombre: str = nombre
        self.__precio: float = precio
        self.__stock: int = stock

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def precio(self) -> float:
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def aumentar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad incorrecta")
        self.__stock += cantidad

    def descontar_stock(self, cantidad):
        if self.stock < cantidad:
            raise ValueError("Stock insuficiente")
        self.__stock -= cantidad

    def __repr__(self):
        return f"{self.nombre:20}  ${self.precio} stock: {self.stock}"


def main():
    mate = Producto("Mate termico", 15000.00, 20)
    print(mate)


if __name__ == "__main__":
    main()
