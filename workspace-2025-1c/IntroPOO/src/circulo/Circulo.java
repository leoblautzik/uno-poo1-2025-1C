package circulo;

public class Circulo {

	private double radio;
	private double xc;
	private double yc;
	private String color;

	public Circulo(double radio, double xc, double yc, String color) {
		this.radio = radio;
		this.xc = xc;
		this.yc = yc;
		this.color = color;
	}
	
	
	@Override
	public String toString() {
		return "Circulo [radio=" + radio + ", color=" + color + "]";
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



	public static void main(String[] args) {
		Circulo c1 = new Circulo(4, 1, 1, "rojo");
		System.out.println(c1);
		System.out.println(c1.area());
		System.out.println(c1.perimetro());
		System.out.println(c1.diametro());
	}

}
