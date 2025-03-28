package nota;

class Nota {

	private int valor;

	/**
	 * pre : valorInicial está comprendido entre 0 y 10. post: inicializa la Nota
	 * con el valor indicado.
	 */
	public Nota(int valorInicial) {
		setValor(valorInicial);

	}

	public boolean esNotaValida(int valor) {
		if (valor < 0 || valor > 10)
			throw new Error("Valor Incorrecto");
		return true;
	}

	/**
	 * post: devuelve el valor numérico de la Nota, comprendido entre 0 y 10.
	 */
	public int obtenerValor() {
		return getValor();
	}

	/**
	 * post: indica si la Nota permite o no la aprobación.
	 */
	public boolean aprobado() {
		return this.valor >= 4;
	}

	/**
	 * post: indica si la Nota implica desaprobación.
	 */
	public boolean desaprobado() {
		return !aprobado();
	}

	/**
	 * pre : nuevoValor está comprendido entre 0 y 10. post: modifica el valor
	 * numérico de la Nota, cambiándolo por nuevoValor, siempre y cuando nuevoValor
	 * sea superior al valor numérico actual de la Nota.
	 */
	public void recuperar(int nuevoValor) {
		if (nuevoValor > this.valor) {
			setValor(nuevoValor);
		}
	}

	private int getValor() {
		return valor;
	}

	private void setValor(int valor) {
		if (esNotaValida(valor))
			this.valor = valor;
	}

	public static void main(String[] args) {
		Nota parcial1 = new Nota(10);
		System.out.println(parcial1.obtenerValor());
		System.out.println(parcial1.aprobado());
		System.out.println(parcial1.desaprobado());
		Nota parcial2 = new Nota(4);
		parcial2.recuperar(-5);
		System.out.println(parcial2.obtenerValor());
		System.out.println(parcial2.aprobado());
		System.out.println(parcial2.desaprobado());

	}

}
