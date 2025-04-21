package profesionales;

public class Cirujano extends Medico {

	public Cirujano(String nombre, String apellido) {
		super(nombre, apellido);
	}

	@Override
	public double calcularHonorario() {
		return super.calcularHonorario() * 1.25;
	}

}
