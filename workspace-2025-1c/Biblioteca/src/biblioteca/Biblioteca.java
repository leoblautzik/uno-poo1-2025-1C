package biblioteca;

import java.util.ArrayList;

public class Biblioteca {

	private ArrayList<Libro> libros;

	public Biblioteca() {
		this.libros = new ArrayList<Libro>();
	}

	public void agregarLibro(String titulo, String autor, Genero genero, int paginas) {
		libros.add(new Libro(titulo, autor, genero, paginas));
	}

	public int cuantosLibros() {
		return this.libros.size();
	}

	public String libroEnLaPosicion(int pos) {
		return this.libros.get(pos - 1).getTitulo();
	}

	public Libro libroConMasPaginas() {
		int posMax = 0;
		int maxPag = this.libros.get(posMax).getCantidadDePaginas();

		for (int i = 1; i < this.libros.size(); i++) {
			if (this.libros.get(i).getCantidadDePaginas() > maxPag) {
				posMax = i;
				maxPag = this.libros.get(i).getCantidadDePaginas();
			}

		}
		return this.libros.get(posMax);

	}

	public void librosPorGeneroLiterario() {
		Genero generos[] = Genero.values();
		int cuantos[] = new int[generos.length];
		for (Libro cadaLibro : libros) {
			int i = cadaLibro.getGenero().ordinal();
			cuantos[i]++;
		}
		for (int i = 0; i < generos.length; i++)
			System.out.println(generos[i] + " " + cuantos[i]);

	}
}
