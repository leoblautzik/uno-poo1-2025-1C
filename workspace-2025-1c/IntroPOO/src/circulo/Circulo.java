package circulo;

import io.Punto;

public class Circulo {

	private double radio;
	private Punto centro;
	private Color color;

	public Circulo(double radio, double xc, double yc, Color color) {
		this.radio = radio;
		this.centro = new Punto(xc, yc);
		this.color = color;
	}

	public Circulo(double radio, Punto centro, Color color) {
		this.radio = radio;
		this.centro = centro;
		this.color = color;
	}
	
	public Circulo() {
		this(1, new Punto(0,0), Color.BLANCO);
	}

	@Override
	public String toString() {
		return "Circulo [radio=" + radio + ", centro=" + centro +", color=" + color + "]";
	}

	public double area() {
		return Math.PI * Math.pow(radio, 2);
	}

	public double perimetro() {
		return Math.PI * this.diametro();
	}

	public double diametro() {
		return 2 * radio;
	}
	
	public double getRadio() {
		return this.radio;
	}

	public static void main(String[] args) {
		Circulo c1 = new Circulo(4, 1, 1, Color.ROJO);
		System.out.println(c1);
		System.out.println(c1.area());
		System.out.println(c1.perimetro());
		System.out.println(c1.diametro());
	}

}
