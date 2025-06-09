package parciales;

import java.io.*;
import java.util.*;

public class GestionVentas {
	private List<Venta> ventas;

	public GestionVentas(String archivoVentas) {
		ventas = new ArrayList<>();
		cargarVentas(archivoVentas);
	}

	private void cargarVentas(String archivo) {
		try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
			String linea;
			while ((linea = br.readLine()) != null) {
				String[] partes = linea.split(",");
				if (partes.length != 4) {
					System.out.println("Línea mal formada: " + linea);
					continue;
				}
				String cliente = partes[0].trim();
				String producto = partes[1].trim();
				int cantidad = Integer.parseInt(partes[2].trim());
				double precio = Double.parseDouble(partes[3].trim());

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
		for (Venta v : ventas) {
			mapa.computeIfAbsent(v.getCliente(), k -> new ArrayList<>()).add(v);
		}
		return mapa;
	}

	public String clienteTop() {
		Map<String, Double> totales = new HashMap<>();
		for (Venta v : ventas) {
			totales.put(v.getCliente(), totales.getOrDefault(v.getCliente(), 0.0) + v.getMontoTotal());
		}
		return totales.entrySet().stream().max(Map.Entry.comparingByValue()).map(Map.Entry::getKey).orElse(null);
	}

	public String productoMasVendido() {
		Map<String, Integer> cantidades = new HashMap<>();
		for (Venta v : ventas) {
			cantidades.put(v.getProducto(), cantidades.getOrDefault(v.getProducto(), 0) + v.getCantidad());
		}
		return cantidades.entrySet().stream().max(Map.Entry.comparingByValue()).map(Map.Entry::getKey).orElse(null);
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
		System.out.println("Producto más vendido: " + gestion.productoMasVendido());
	}
}
