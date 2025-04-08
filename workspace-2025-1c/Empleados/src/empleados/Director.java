package empleados;

public class Director extends Gerente {

	private double adicional;

	public Director(String nombre, double sueldoBasico, Fecha fechaDeNacimiento, String departamento,
			double adicional) {
		super(nombre, sueldoBasico, fechaDeNacimiento, departamento);
		this.adicional = adicional;
	}

	@Override
	public double getSalario() {
		return super.getSalario() + this.adicional;

	}
	
	@Override
	public String toString() {
		return "Director-" + super.toString();
	}
 
}
