package juegoDeEstrategia;

public abstract class Unidad {

	private int salud;
	private int danio;
	private int posicion;

	public int getSalud() {
		return salud;
	}

	public int getDanio() {
		return danio;
	}
	public int getPosicion() {
		return this.posicion;
	}

	public Unidad(int salud, int danio, int posicion) {
		this.salud = salud;
		this.danio = danio;
		this.posicion = posicion;
	}

	

	public void recibirDanio(int danio) {
		this.salud -= danio;
	}

	public boolean estaMuerto() {
		return this.salud <= 0;
	}

	public int distancia(Unidad enemigo) {
		return Math.abs(this.getPosicion() - enemigo.getPosicion());
	}

	public abstract void atacar(Unidad enemigo);

}
