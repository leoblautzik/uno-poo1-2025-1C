"""
Archivo de entrada: productos.csv con descripcion, categoria, precio, stock para cada producto
Laptop, Electrónica 1000, 5
Smartphone, Electrónica, 700, 10
Mesa, Muebles, 150, 15
Silla, Muebles, 80, 30
a. Implementar la class GestionProductos que guarde en una lista todos los productos leídos del archivo.
b. Debe proveer un metodo que devuelve un diccionario donde la key sea la categoría, y el value asociado, una lista con los productos de esa categoría.
c. Debe proveer un metodo que devuelva la categoríá más valiosa, o sea que la cantidad de productos en stock multiplicado por su precio, sea la mayor.
En el caso del ejemplo:
Electrónica vale 1000 * 5 + 700 * 10 = 12000
Muebles vale 150 * 15 + 80 * 30 = 4650
Deberá devolver Electrónica
Nota: Se debe implementar la class Producto

"""

from io import open


class Producto:
    def __init__(self, descripcion, categoria, precio, stock):
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.descripcion} {self.precio} {self.stock}"


class GestionProductos:
    def __init__(self):
        self.productos = []

    def __str__(self):
        s = ""
        for p in self.productos:
            s = s + str(p) + "\n"
        return s

    def leer_productos(self, archivo):
        with open(archivo, "r", encoding="UTF-8") as ap:
            for line in ap:
                datos = line.split(",")
                try:
                    self.productos.append(
                        Producto(datos[0], datos[1], float(datos[2]), int(datos[3]))
                    )
                except ValueError:
                    pass

    def productos_por_categoria(self):
        ppc = {}
        for pr in self.productos:
            lista_p = ppc.get(pr.categoria, [])
            lista_p.append(pr)
            # ppc[pr.categoria] = lista_p
            ppc.update({pr.categoria: lista_p})

        return ppc

    def categoria_mas_valiosa(self):
        ppc_v = {}
        for pr in self.productos:
            valor = ppc_v.get(pr.categoria, 0)
            valor += pr.precio * pr.stock
            ppc_v.update({pr.categoria: valor})

        max_valor = max(ppc_v.values())
        max_categoria = ""

        for cate, valor in ppc_v.items():
            if valor == max_valor:
                max_categoria = cate

        return max_categoria, max_valor


def main():
    gp = GestionProductos()
    gp.leer_productos("productos.csv")
    print(gp)
    print(gp.productos_por_categoria())
    print(gp.categoria_mas_valiosa())


if __name__ == "__main__":
    main()
