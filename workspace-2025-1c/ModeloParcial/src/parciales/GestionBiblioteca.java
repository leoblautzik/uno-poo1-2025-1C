package parciales;

import java.io.*;
import java.util.*;

public class GestionBiblioteca {
	private List<Libro> libros;

	public GestionBiblioteca() {
		libros = new ArrayList<>();
	}

	public void cargarLibros(String nombreArchivo) {
		try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {
			String linea;
			while ((linea = br.readLine()) != null) {
				String[] partes = linea.split(",");
				try {
					if (partes.length != 4) {
						throw new LineaMalFormadaException();
					}
				} catch (LineaMalFormadaException lmfe) {
					System.out.println("Línea ignorada por formato incorrecto: " + linea);
				}

				String titulo = partes[0].trim();
				String autor = partes[1].trim();
				String genero = partes[2].trim();
				int cantidad;

				try {
					cantidad = Integer.parseInt(partes[3].trim());
				} catch (NumberFormatException e) {
					System.out.println("Cantidad inválida en línea: " + linea);
					continue;
				}

				libros.add(new Libro(titulo, autor, genero, cantidad));
			}
		} catch (FileNotFoundException e) {
			System.out.println("Archivo no encontrado: " + nombreArchivo);
		} catch (IOException e) {
			System.out.println("Error al leer el archivo: " + e.getMessage());
		}
	}

	public Map<String, List<Libro>> librosPorGenero() {
		Map<String, List<Libro>> mapa = new HashMap<>();
		for (Libro libro : libros) {
			List<Libro> l = mapa.getOrDefault(libro.getGenero(), new ArrayList<Libro>());
			l.add(libro);
			mapa.put(libro.getAutor(), l);
		}
		return mapa;
	}

	public String autorConMasLibrosDisponibles() {
		Map<String, Integer> conteo = new HashMap<>();
		int cant_libros;
		for (Libro libro : libros) {
			cant_libros = conteo.getOrDefault(libro.getGenero(), 0) + libro.getCantidadDisponible();
			conteo.put(libro.getAutor(), cant_libros);
		}

		String autorMax = null;
		int max = 0;
		for (Map.Entry<String, Integer> entry : conteo.entrySet()) {
			if (entry.getValue() > max) {
				max = entry.getValue();
				autorMax = entry.getKey();
			}
		}
		if (autorMax != null)
			return autorMax + ": " + max + " libros disponibles.";
		else
			return "Sin datos.";
	}

	public static void main(String[] args) {
		GestionBiblioteca gestion = new GestionBiblioteca();
		gestion.cargarLibros("libros.csv");

		System.out.println("2.b: Diccionario por género:");
		Map<String, List<Libro>> librosPorGenero = gestion.librosPorGenero();
		for (String genero : librosPorGenero.keySet()) {
			System.out.println(genero + ": " + librosPorGenero.get(genero));
		}

		System.out.println("\n2.c: Autor con más libros disponibles:");
		System.out.println(gestion.autorConMasLibrosDisponibles());
	}
}
