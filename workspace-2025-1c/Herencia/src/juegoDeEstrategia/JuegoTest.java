package juegoDeEstrategia;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class JuegoTest {

	@Test
	void soldadoAtacaSoldadoTest() {
		Soldado rambo = new Soldado(1);
		Soldado ryan = new Soldado(1);
		System.out.println(rambo instanceof Soldado);
		rambo.atacar(ryan);
		assertEquals(190, ryan.getSalud());
		assertEquals(90, rambo.getEnergia());
	}
	
	@Test
	void soldadoLejosTest() {
		Soldado rambo = new Soldado(1);
		Soldado ryan = new Soldado(10);
		assertFalse(rambo.puedeAtacar(ryan));
	}
	@Test
	void atacaHastaquedarSinEnergiaTest() {
		Soldado rambo = new Soldado(1);
		Soldado ryan = new Soldado(1);
		for(int i=0; i<10; i++) {
			rambo.atacar(ryan);
		}
		assertFalse(rambo.puedeAtacar(ryan));
		assertTrue(ryan.puedeAtacar(rambo));
	}
	
	@Test
	void atacaHastaquedarSinFlechasTest() {
		Soldado rambo = new Soldado(1);
		Arquero legolas = new Arquero(5);
		for(int i=0; i<20; i++) {
			legolas.atacar(rambo);
		}
		assertFalse(legolas.puedeAtacar(rambo));
		assertEquals(100,rambo.getSalud());
		assertEquals(0, legolas.getFlechas());
	}
	

}
