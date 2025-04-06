package circulo;

public class CoronaCircular {
	private Circulo chiquito;
	private Circulo grandote;

	public CoronaCircular(double radioMayor, double radioMenor, double xc, double yc, Color color) {
		this.chiquito = new Circulo(radioMenor, xc, yc, color);
		this.grandote = new Circulo(radioMayor, xc, yc, color);
	}

	public double getRadioMenor() {
		return this.chiquito.getRadio();
	}

	public double getRadioMayor() {
		return this.grandote.getRadio();
	}

	public double getArea() {
		return this.grandote.area() - this.chiquito.area();

	}
	
	public double getPerimetroInterior() {
		return this.chiquito.perimetro();
	}

}
