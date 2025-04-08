package empleados;

public class Empleado {
	
	private String nombre = " ";
	private double sueldoBasico = 0;
	private Fecha fechaDeNacimiento;
	
	
	
	public Empleado(String nombre, double sueldoBasico, Fecha fechaDeNacimiento) {
		this.nombre = nombre;
		this.sueldoBasico = sueldoBasico;
		this.fechaDeNacimiento = fechaDeNacimiento;
	}
	
	public double getSalario() {
		return this.sueldoBasico;
	}
	
	

	@Override
	public String toString() {
		return "Empleado [nombre=" + nombre + ", sueldoBasico=" + getSalario() + "]";
	}



	public static void main(String[] args) {
		Empleado juancito = new Empleado("Juan", 1500000, new Fecha());
		System.out.println(juancito);
		
		Gerente carlitos = new Gerente("Carlos", 2000000, new Fecha(), "Compras");
		System.out.println(carlitos);
		
		Director dire = new Director("Fernando", 2100000, new Fecha(), "Suministros", 500000);
		System.out.println(dire);

	}



	

}
