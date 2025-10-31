"""
Archivo de entrada: productos.csv con descripcion, categoria, precio,
stock para cada producto
Laptop, Electrónica 1000, 5
Smartphone, Electrónica, 700, 10
Mesa, Muebles, 150, 15
Silla, Muebles, 80, 30
Implementar la class GestionProductos que guarde en una lista todos
los productos leídos del archivo.
Debe proveer un metodo que devuelve un diccionario donde la key
sea la categoría, y el value asociado, una lista con los productos
de esa categoría.
Debe proveer un metodo que devuelva la categoríá más valiosa,
o sea que la cantidad de productos en stock multiplicado por su precio,
sea la mayor.
En el caso del ejemplo:
Electrónica vale 1000 * 5 + 700 * 10 = 12000
Muebles vale 150 * 15 + 80 * 30 = 4650
Deberá devolver Electrónica
Nota: Se debe implementar la class Producto
"""


class Producto:
    def __init__(self, descripcion, categoria, precio, stock) -> None:
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __repr__(self) -> str:
        return (
            f"Descripción: {self.descripcion}, Categoria: {self.categoria}"
            f", Precio: ${self.precio}, Stock: {self.stock}"
        )

    def __str__(self) -> str:
        return f"{self.descripcion}, {self.categoria}"

    def __eq__(self, other: object, /) -> bool:
        if isinstance(other, Producto):
            return (
                self.categoria == other.categoria
                and self.descripcion == other.descripcion
            )
        return False

    def __hash__(self):
        return hash(self.categoria + self.descripcion)


class GestionProducto:
    def __init__(self) -> None:
        self.productos: list[Producto] = []

    def leer_productos(self, archivo):
        with open(archivo, "r", encoding="UTF-8") as pr:
            for cada_linea in pr:
                datos = cada_linea.strip().split(",")
                self.productos.append(
                    Producto(datos[0], datos[1], float(datos[2]), int(datos[3]))
                )
        pr.close()

    def productos_por_categoria(self) -> dict[str, list[Producto]]:
        ppc: dict[str, list[Producto]] = {}

        for producto in self.productos:
            if producto.categoria not in ppc.keys():
                lp = []
            else:
                lp = ppc[producto.categoria]
            lp.append(producto)
            ppc[producto.categoria] = lp

        return ppc

    def categoria_mas_valiosa(self) -> tuple[str, float]:
        ppc = self.productos_por_categoria()
        dic_cat_valor: dict[str, float] = {}
        for cate, lista_prod in ppc.items():
            valor = 0
            for prod in lista_prod:
                valor += prod.precio * prod.stock
            dic_cat_valor[cate] = valor

        return max(dic_cat_valor.items(), key=lambda item: item[1])


def main():
    gp = GestionProducto()
    gp.leer_productos("productos.csv")
    print(gp.productos)
    print(gp.productos_por_categoria())
    print(gp.categoria_mas_valiosa())


if __name__ == "__main__":
    main()
