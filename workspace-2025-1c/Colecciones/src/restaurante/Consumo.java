package restaurante;

public class Consumo {
	
	private int codigo;
	private String descripcion;
	private double precio;

	public Consumo(int codigo, String descripcion, double precio) {
		this.codigo = codigo;
		this.descripcion = descripcion;
		this.precio = precio;
	}
	public double getPrecio() {
		return precio;
	}
	
	@Override
	public String toString() {
		return "codigo: " + codigo + " " + descripcion + " " + precio;
	}
	
	
	

}
