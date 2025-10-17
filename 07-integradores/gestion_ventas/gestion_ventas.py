from io import open


class LineaMalFormada(Exception):
    pass


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
                    datos = linea.strip().split(",")
                    try:
                        if len(datos) != 4:
                            raise LineaMalFormada
                        cliente = datos[0].strip()
                        producto = datos[1].strip()
                        cantidad_str = datos[2].strip()
                        precio_str = datos[3].strip()
                        try:
                            cantidad = int(cantidad_str)
                            precio = float(precio_str)
                            venta = Venta(cliente, producto, cantidad, precio)
                            self.ventas.append(venta)
                        except ValueError:
                            print(f"Error en conversión de números: {linea}")
                    except LineaMalFormada:
                        print(f"Error en formato de línea: {linea}")
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")

    def ventas_por_cliente(self):
        ventas_por_cliente = {}
        for venta in self.ventas:
            ventas_por_cliente.setdefault(venta.cliente, []).append(venta)
        return ventas_por_cliente

    def cliente_top(self):
        totales_por_cliente = {}
        for venta in self.ventas:
            totales_por_cliente[venta.cliente] = (
                totales_por_cliente.get(venta.cliente, 0) + venta.monto_total()
            )
        # cliente_t = max(totales_por_cliente, key=totales_por_cliente.get)
        clientes_t = []
        if totales_por_cliente:
            # mayor = float("-inf")
            # for monto in totales_por_cliente.values():
            #     if monto > mayor:
            #         mayor = monto
            mayor = max(totales_por_cliente.values())
            for cliente, monto in totales_por_cliente.items():
                if monto == mayor:
                    clientes_t.append(cliente)

        return clientes_t

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
        print(f"{cliente}: {[f'{v.producto} x {v.cantidad}' for v in ventas]}")

    print("\nCliente top:", gestion.cliente_top())
    print("Producto más vendido:", gestion.producto_mas_vendido())


if __name__ == "__main__":
    main()
