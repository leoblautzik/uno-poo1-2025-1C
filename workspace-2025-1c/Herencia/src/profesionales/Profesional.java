package profesionales;

public abstract class Profesional implements Comparable<Profesional> {
	
	private static double honorarioBasico=500000;
	
	public static void setHonorarioBasico(double nuevoValor) {
		Profesional.honorarioBasico = nuevoValor;
	}
	public static double getHonorarioBasico() {
		return Profesional.honorarioBasico;
	}
	
	@Override
	public String toString() {
		return "Profesional [nombre=" + nombre + ", apellido=" + apellido + ", calcularHonorario()="
				+ calcularHonorario() + "]";
	}

	private String nombre;
	private String apellido;
	

	public Profesional(String nombre, String apellido) {
		this.nombre = nombre;
		this.apellido = apellido;
	}

	public abstract double calcularHonorario();

	@Override
	public int compareTo(Profesional otro) {
//		if (this.calcularHonorario() < otro.calcularHonorario())
//			return -1;
//		if (this.calcularHonorario() > otro.calcularHonorario())
//			return 1;
//		return 0;
		
		return (-1) * Double.compare(this.calcularHonorario(), otro.calcularHonorario());
	}

}
