package colecciones;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.Test;

class ColleccionesTest {

	@Test
	void esSublistaTest() {
		Practica p1 = new Practica();
		List<Integer> l1 = Arrays.asList(22,14,6);
		List<Integer> l2 = Arrays.asList(39,41,17,22,14,6,3,11,73,81);
		assertTrue(p1.esSublista(l1, l2));
	}
	@Test
	void esSublistaAlFinalTest() {
		Practica p1 = new Practica();
		List<Integer> l1 = Arrays.asList(11,73,81);
		List<Integer> l2 = Arrays.asList(39,41,17,22,14,6,3,11,73,81);
		assertTrue(p1.esSublista(l1, l2));
	}
	@Test
	void esSublistaAlPrincipioTest() {
		Practica p1 = new Practica();
		List<Integer> l1 = Arrays.asList(39,41,17);
		List<Integer> l2 = Arrays.asList(39,41,17,22,14,6,3,11,73,81);
		assertTrue(p1.esSublista(l1, l2));
	}
	@Test
	void noEsSublistaTest() {
		Practica p1 = new Practica();
		List<Integer> l1 = Arrays.asList(39,41,17);
		List<Integer> l2 = Arrays.asList(39,4,41,22,17,6,3,11,73,81);
		assertFalse(p1.esSublista(l1, l2));
	}
	
	@Test
	void terminalDeTeletipoTest() {
		Practica p1 = new Practica();
		String esperado = "ae";
		String obtenido = p1.terminalDeTeletipo("abc//d/e");
		assertEquals(esperado, obtenido);
		
	}
	@Test
	void terminalDeTeletipoPilaVaciaTest() {
		Practica p1 = new Practica();
		String esperado = "e";
		String obtenido = p1.terminalDeTeletipo("a///d/e");
		assertEquals(esperado, obtenido);
		
	}
	@Test
	void terminalDeTeletipoSoloBarrasTest() {
		Practica p1 = new Practica();
		String esperado = "";
		String obtenido = p1.terminalDeTeletipo("////");
		assertEquals(esperado, obtenido);
		
	}
	@Test
	void terminalDeTeletipoConLimpiadorTest() {
		Practica p1 = new Practica();
		String esperado = "de";
		String obtenido = p1.terminalDeTeletipo("abc&de");
		assertEquals(esperado, obtenido);
		
	}
}
