package parciales;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GestionVentas {
	private List<Venta> ventas;

	public GestionVentas(String archivoVentas) {
		ventas = new ArrayList<Venta>();
		cargarVentas(archivoVentas);
	}

	private void cargarVentas(String archivo) {
		try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
			String linea;
			while ((linea = br.readLine()) != null) {
				String[] datos = linea.split(",");
				if (datos.length != 4) {
					System.out.println("Línea mal formada: " + linea);
					continue;
				}
				String cliente = datos[0].trim();
				String producto = datos[1].trim();
				int cantidad = Integer.parseInt(datos[2].trim());
				double precio = Double.parseDouble(datos[3].trim());

				ventas.add(new Venta(cliente, producto, cantidad, precio));
			}
		} catch (IOException e) {
			System.out.println("Error leyendo el archivo: " + e.getMessage());
		} catch (NumberFormatException e) {
			System.out.println("Error en conversión de números: " + e.getMessage());
		}
	}

	public Map<String, List<Venta>> ventasPorCliente() {
		Map<String, List<Venta>> mapa = new HashMap<>();
		List<Venta> l;
		for (Venta v : ventas) {
			l = mapa.getOrDefault(v.getCliente(), new ArrayList<Venta>());
			l.add(v);
			mapa.put(v.getCliente(), l);
		}
		return mapa;
	}

	public String clienteTop() {
		Map<String, Double> totales = new HashMap<>();
		double total;
		double mayor;
		for (Venta v : ventas) {
			total = totales.getOrDefault(v.getCliente(), 0.0) + v.getMontoTotal();
			totales.put(v.getCliente(), total);
		}
		mayor = Collections.max(totales.values());
		String clienteT = null;
		for (Map.Entry<String, Double> entry : totales.entrySet()) {
			if (entry.getValue() == mayor ) {
				clienteT = entry.getKey();
			}
		}
		return clienteT;
		
	}

	public List<String> clientesTop() {
		Map<String, Double> totales = new HashMap<>();
		double total;
		double mayor;
		for (Venta v : ventas) {
			total = totales.getOrDefault(v.getCliente(), 0.0) + v.getMontoTotal();
			totales.put(v.getCliente(), total);
		}
		mayor = Collections.max(totales.values());
		List<String> clientesT = new ArrayList<String>();
		for (Map.Entry<String, Double> entry : totales.entrySet()) {
			if (entry.getValue() == mayor ) {
				clientesT.add(entry.getKey());
			}
		}
		return clientesT;
		
	}
	public String productoMasVendido() {
		Map<String, Integer> cantidades = new HashMap<>();
		for (Venta v : ventas) {
			cantidades.put(v.getProducto(), cantidades.getOrDefault(v.getProducto(), 0) + v.getCantidad());
		}
		
		Integer mayor = Collections.max(cantidades.values());
		String productoMasVendido = null;
		for (Map.Entry<String, Integer> entry : cantidades.entrySet()) {
			if (entry.getValue() == mayor ) {
				mayor = entry.getValue();
				productoMasVendido = entry.getKey();
			}
		}
		return productoMasVendido;
		
		
	}

	public static void main(String[] args) {
		GestionVentas gestion = new GestionVentas("ventas.csv");

		System.out.println("Ventas por cliente:");
		for (Map.Entry<String, List<Venta>> entry : gestion.ventasPorCliente().entrySet()) {
			System.out.print(entry.getKey() + ": ");
			for (Venta v : entry.getValue()) {
				System.out.print(v.getProducto() + " x" + v.getCantidad() + "  ");
			}
			System.out.println();
		}

		System.out.println("\nCliente top: " + gestion.clienteTop());
		System.out.println("\nClientes top: " + gestion.clientesTop());
		System.out.println("Producto más vendido: " + gestion.productoMasVendido());
	}
}
