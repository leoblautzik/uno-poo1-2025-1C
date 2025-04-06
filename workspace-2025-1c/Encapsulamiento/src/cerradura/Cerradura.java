package cerradura;

class Cerradura {
	private int key;
	private int cantidadDeFallosConsecutivosQueLaBloquean;
	private boolean estaAbierta;
	private boolean estaBloqueada;
	private int contadorAperturasExitosas = 0;
	private int contadorAperturasFallidas = 0;
	private int contadorFallosConsecutivos = 0;

	public Cerradura(int claveDeApertura, int cantidadDeFallosConsecutivosQueLaBloquean) {
		this.key = claveDeApertura;
		this.cantidadDeFallosConsecutivosQueLaBloquean = cantidadDeFallosConsecutivosQueLaBloquean;
	}

	public boolean abrir(int clave) {
		if (this.fueBloqueada()) {
			throw new Error("Cerradura bloqueada");
		}
		if (this.estaCerrada()) {
			if (clave == this.key) {
				this.estaAbierta = true;
				this.contadorAperturasExitosas++;
				this.contadorFallosConsecutivos = 0;
				return true;
			} else {
				this.contadorAperturasFallidas++;
				this.contadorFallosConsecutivos++;
				if (this.contadorFallosConsecutivos >= this.cantidadDeFallosConsecutivosQueLaBloquean) {
					this.estaBloqueada = true;
				}
				return false;
			}
		}
		return false;
	}

	public void cerrar() {
		this.estaAbierta = false;
	}

	public boolean estaAbierta() {
		return this.estaAbierta;
	}

	public boolean estaCerrada() {
		return !this.estaAbierta;
	}

	public boolean fueBloqueada() {
		return this.estaBloqueada;
	}

	public int contarAperturasExitosas() {
		return this.contadorAperturasExitosas;
	}

	public int contarAperturasFallidas() {
		return this.contadorAperturasFallidas;
	}

}