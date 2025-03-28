package tarjetaBaja;

class TarjetaBaja {

	private double saldo;
	private int viajesEnColectivo;
	private int viajesEnSubte;

	/**
	 * post: saldo de la Tarjeta en saldoInicial.
	 */
	public TarjetaBaja(double saldoInicial) {
		if (saldoInicial < 0)
			throw new Error("El importe debe ser >= 0");
		this.saldo = saldoInicial;
		this.viajesEnColectivo = 0;
		this.viajesEnSubte = 0;
	}

	/**
	 * post: devuelve el saldo actual de la Tarjeta
	 */
	public double obtenerSaldo() {
		return this.saldo;
	}

	/**
	 * post: agrega el monto al saldo de la Tarjeta.
	 */
	public void cargar(double monto) {
		if (monto <= 0)
			throw new Error("El importe debe ser >= 0");
		this.saldo += monto;
	}

	/**
	 * pre : saldo suficiente. post: utiliza 21.50 del saldo para un viaje en
	 * colectivo.
	 */
	public void pagarViajeEnColectivo() {
		if (this.saldo >= 21.50) {
			this.saldo -= 21.50;
			this.viajesEnColectivo++;
		}

	}

	/**
	 * pre : saldo suficiente. post: utiliza 19.50 del saldo para un viaje en subte.
	 */
	public void pagarViajeEnSubte() {
		if (this.saldo >= 19.50) {
			this.saldo -= 19.50;
			this.viajesEnSubte++;
		}
	}

	/**
	 * post: devuelve la cantidad de viajes realizados.
	 */
	public int contarViajes() {
		return this.viajesEnColectivo + this.viajesEnSubte;
	}

	/**
	 * post: devuelve la cantidad de viajes en colectivo.
	 */
	public int contarViajesEnColectivo() {
		return this.viajesEnColectivo;
	}

	/**
	 * post: devuelve la cantidad de viajes en subte.
	 */
	public int contarViajesEnSubte() {
		return this.viajesEnSubte;
	}

	public static void main(String[] args) {
		TarjetaBaja tb = new TarjetaBaja(100);
		System.out.println(tb.obtenerSaldo());
		tb.pagarViajeEnColectivo();
		tb.pagarViajeEnSubte();
		tb.pagarViajeEnSubte();
		System.out.println(tb.obtenerSaldo());
		System.out.println(tb.contarViajesEnColectivo());
		System.out.println(tb.contarViajesEnSubte());
		System.out.println(tb.contarViajes());
		

	}
}
