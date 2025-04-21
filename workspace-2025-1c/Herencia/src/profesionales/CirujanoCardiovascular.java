package profesionales;

public class CirujanoCardiovascular extends Cirujano {

	public CirujanoCardiovascular(String nombre, String apellido) {
		super(nombre, apellido);
	}

	@Override
	public double calcularHonorario() {
		return super.calcularHonorario() * 1.25;
	}
}
