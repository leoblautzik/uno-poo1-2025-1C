package encapsulamiento;

public class Auto {

	private Motor motor;
	private String marca;

	public Auto(String marca, Motor motor) {
		this.marca = marca;
		this.motor = motor;
	}
	public Auto(String marca, String tipoDeMotor) {
		this.marca = marca;
		this.motor = new Motor(tipoDeMotor);
	}
	
	public String getMarca() {
		return this.marca;
	}
	
	public String getTipoDeMotor() {
		return this.motor.getTipoDeMotor();
	}

	
	@Override
	public String toString() {
		return "Marca: " + this.getMarca() + ", Tipo de motor: " + this.getTipoDeMotor();  
	}


}
