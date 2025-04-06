package cerradura;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class CerraduraTest {

	@Test
	void estadoInicialTest() {
		Cerradura trabex = new Cerradura(123, 3);
		assertFalse(trabex.estaAbierta());
	}

	@Test
	void primerAperturaExitosaTest() {
		Cerradura trabex = new Cerradura(123, 3);
		trabex.abrir(123);
		assertTrue(trabex.estaAbierta());
		assertEquals(1, trabex.contarAperturasExitosas());
	}
	
	@Test 
	void intentoAbrirCerraduraAbiertaTest() {
		Cerradura trabex = new Cerradura(123, 3);
		trabex.abrir(123);
		trabex.abrir(111);		
	}

	@Test
	void primerAperturaFallidaTest() {
		Cerradura trabex = new Cerradura(123, 3);
		trabex.abrir(122);
		assertFalse(trabex.estaAbierta());
		assertEquals(0, trabex.contarAperturasExitosas());
		assertEquals(1, trabex.contarAperturasFallidas());
	}

	@Test
	void dosAperturasFallidasYLuegoAciertoTest() {
		Cerradura trabex = new Cerradura(123, 3);
		trabex.abrir(122);
		assertFalse(trabex.estaAbierta());
		trabex.abrir(132);
		assertFalse(trabex.estaAbierta());
		trabex.abrir(123);
		assertTrue(trabex.estaAbierta());
		assertEquals(1, trabex.contarAperturasExitosas());
		assertEquals(2, trabex.contarAperturasFallidas());
	}

	@Test
	void tresAperturasFallidasYbloqueoTest() {
		Cerradura trabex = new Cerradura(123, 3);
		trabex.abrir(122);
		assertFalse(trabex.estaAbierta());
		trabex.abrir(132);
		assertFalse(trabex.estaAbierta());
		trabex.abrir(223);
		assertTrue(trabex.fueBloqueada());
		assertEquals(0, trabex.contarAperturasExitosas());
		assertEquals(3, trabex.contarAperturasFallidas());
	}

	@Test
	void intentoAbrirPeroFueBloqueadaTest() {
		Cerradura trabex = new Cerradura(123, 3);
		trabex.abrir(122);
		assertFalse(trabex.estaAbierta());
		trabex.abrir(132);
		assertFalse(trabex.estaAbierta());
		trabex.abrir(223);
		assertTrue(trabex.fueBloqueada());
		assertThrows(Error.class, () -> trabex.abrir(123));

	}
	@Test
	void cienAperturasExitosasTest() {
		Cerradura trabex = new Cerradura(123, 3);
		for(int i=0; i<100; i++) {
			trabex.abrir(123);
			trabex.cerrar();
			
		}
		assertEquals(100, trabex.contarAperturasExitosas());
	}

}
