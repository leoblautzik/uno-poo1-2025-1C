package profesionales;

public class Endodoncista extends Dentista {
	
	public Endodoncista(String nombre, String apellido) {
		super(nombre, apellido);
	}

	@Override
	public double calcularHonorario() {
		return super.calcularHonorario() * 1.25;
	}
}
