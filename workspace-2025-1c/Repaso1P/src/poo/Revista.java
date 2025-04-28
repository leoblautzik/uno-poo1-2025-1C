package poo;

public class Revista extends Publicacion {
	private int edicionesAnuales;
	
	public Revista(String titulo, double PrecioBase, int edicionesAnuales) {
		super(titulo, PrecioBase);
		this.edicionesAnuales=edicionesAnuales;
	}
	public double getPrecio() {
		double precio = super.getPrecio();
		if (this.edicionesAnuales > 12){
			precio *= 1.05;
		}
		return precio;
	}
	
	@Override
	public String toString() {
		//String.format("%.3f",7.0004);
		return "Titulo: " + super.getTitulo() + ", Ediciones anuales " + this.edicionesAnuales + ", Precio: " + String.format("%.2f", this.getPrecio());
	}

	
}
