package profesionales;

public class Dentista extends Profesional {

	public Dentista(String nombre, String apellido) {
		super(nombre, apellido);
	}

	@Override
	public double calcularHonorario() {
		return Profesional.getHonorarioBasico();
	}

}
