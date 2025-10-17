from io import open


class Venta:
    def __init__(self, cliente, producto, cantidad, precio_unitario):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def monto_total(self):
        return self.cantidad * self.precio_unitario


class GestionVentas:
    def __init__(self, archivo_ventas):
        self.ventas = []
        self.cargar_ventas(archivo_ventas)

    def cargar_ventas(self, archivo):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    partes = linea.strip().split(",")
                    if len(partes) != 4:
                        print(f"Línea mal formada: {linea}")
                        continue
                    cliente, producto, cantidad_str, precio_str = partes
                    try:
                        cantidad = int(cantidad_str)
                        precio = float(precio_str)
                        venta = Venta(
                            cliente.strip(), producto.strip(), cantidad, precio
                        )
                        self.ventas.append(venta)
                    except ValueError:
                        print(f"Error en conversión de números: {linea}")
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")

    def ventas_por_cliente(self):
        resultado = {}
        for venta in self.ventas:
            resultado.setdefault(venta.cliente, []).append(venta)
        return resultado

    def cliente_top(self):
        totales = {}
        for venta in self.ventas:
            totales[venta.cliente] = totales.get(venta.cliente, 0) + venta.monto_total()
        if totales:
            return max(totales, key=totales.get)
        return None

    def producto_mas_vendido(self):
        contador = {}
        for venta in self.ventas:
            contador[venta.producto] = contador.get(venta.producto, 0) + venta.cantidad
        if contador:
            return max(contador, key=contador.get)
        return None


# Código de prueba


def main():
    gestion = GestionVentas("ventas.csv")
    print("Ventas por cliente:")
    for cliente, ventas in gestion.ventas_por_cliente().items():
        print(f"{cliente}: {[f'{v.producto} x{v.cantidad}' for v in ventas]}")

    print("\nCliente top:", gestion.cliente_top())
    print("Producto más vendido:", gestion.producto_mas_vendido())


if __name__ == "__main__":
    main()
