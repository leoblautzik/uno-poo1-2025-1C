package poo;

import java.util.ArrayList;

public class Editorial {

	public static void main(String[] args) {

		ArrayList<Publicacion> publicaciones = new ArrayList<Publicacion>();
		publicaciones.add(new Revista("Chacra", 5000.00, 12));
		publicaciones.add(new Libro("Librito", 25000.00, 900));
		
		for(Publicacion p : publicaciones) {
			System.out.println(p);
		}
	}

}
