package juegoDeEstrategia;

public class Soldado extends Unidad implements Bebedor {

	private int energia = 100;

	public Soldado(int posicion) {
		super(200, 10, posicion);
	}

	public int getEnergia() {
		return this.energia;
	}

	@Override
	public void atacar(Unidad enemigo) {

		if (this.puedeAtacar(enemigo)) {
			this.energia -= 10;
			enemigo.recibirDanio(10);
		}
	}

	public boolean puedeAtacar(Unidad enemigo) {
		if (enemigo.estaMuerto()) {
			throw new Error("No podes atacar a un muerto");
		}

		return this.distancia(enemigo) == 0 && !this.estaMuerto() && this.energia >= 10;
	}

	@Override
	public void beberAgua() {
		this.energia = 100;
	}

}
