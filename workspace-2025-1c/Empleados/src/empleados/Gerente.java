package empleados;

public class Gerente extends Empleado {
	private String departamento;
	

	public Gerente(String nombre, double sueldoBasico, Fecha fechaDeNacimiento, String departamento) {
		super(nombre, sueldoBasico, fechaDeNacimiento);
		this.departamento = departamento;
	}


	@Override
	public String toString() {
		return "Gerente [departamento=" + departamento + "  "+ super.toString();
	}
	
	public double getSalario() {
		return super.getSalario()*1.2;
	}
	
	



	

	

}
