package poo;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class publicacionesTest {

	@Test
	void libroMenosde300Paginas() {
		Libro l = new Libro("La vida de Alguien", 100.00, 299);
		assertEquals(100.00, l.getPrecio());
		
	}

	@Test
	void libroDe300Paginas() {
		Libro l = new Libro("La vida de Alguien", 100.00, 300);
		assertEquals(100.00, l.getPrecio());
		
	}

	@Test
	void libroDeMasDe300Paginas() {
		Libro l = new Libro("La vida de Alguien", 100.00, 301);
		assertEquals(110.00, l.getPrecio(), 0.001);
		
	}
}
