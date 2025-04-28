package poo;

public abstract class Publicacion {
	private String titulo;
	private double precioBase;
	
	public Publicacion(String titulo, double precioBase) {
		this.titulo=titulo;
		this.precioBase=precioBase;
	}
	
	public double getPrecio() {
		return this.precioBase;
	}
	
	public String getTitulo() {
		return this.titulo;
	}
	

}
