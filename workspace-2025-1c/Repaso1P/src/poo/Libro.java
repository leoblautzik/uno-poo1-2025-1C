package poo;

public class Libro extends Publicacion {
	
	private int paginas;

	public Libro(String titulo,double PrecioBase, int paginas) {
		super(titulo, PrecioBase);
		this.paginas=paginas;
	}
	
	public double getPrecio() {
		double precio = super.getPrecio();
		if (this.paginas > 300){
			precio *= 1.10;
		}
		return precio;
	}
	
	@Override
	public String toString() {
		return "Titulo: " + super.getTitulo() + ", Paginas: " + this.paginas + ", Precio: " + String.format("%.2f", this.getPrecio());
	}

}
