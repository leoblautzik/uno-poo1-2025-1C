package juegoDeEstrategia;

public class Arquero extends Unidad {

	public Arquero(int salud, int danio, int posicion) {
		super(salud, danio, posicion);
		// TODO Auto-generated constructor stub
	}

	

	private int flechas = 20;

	public Arquero(int posicion) {
		super(50, 5, posicion);
	}
	
	public int getFlechas() {
		return this.flechas;
	}

	@Override
	public void atacar(Unidad enemigo) {

		if (this.puedeAtacar(enemigo)) {
			this.flechas--;
			enemigo.recibirDanio(5);
		}
	}

	public boolean puedeAtacar(Unidad enemigo) {
		if (enemigo.estaMuerto()) {
			throw new Error("No podes atacar a un muerto");
			
		}

		return this.distancia(enemigo) >= 2 && this.distancia(enemigo) <= 5  
				&& !this.estaMuerto() && this.flechas > 0;
				
	}

}
