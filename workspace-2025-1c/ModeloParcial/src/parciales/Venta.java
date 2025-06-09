package parciales;

public class Venta {

	private String cliente;
	private String producto;
	private int cantidad;
	private double precioUnitario;

	public Venta(String cliente, String producto, int cantidad, double precioUnitario) {
		this.cliente = cliente;
		this.producto = producto;
		this.cantidad = cantidad;
		this.precioUnitario = precioUnitario;
	}

	public String getCliente() {
		return cliente;
	}

	public String getProducto() {
		return producto;
	}

	public int getCantidad() {
		return cantidad;
	}

	public double getMontoTotal() {
		return cantidad * precioUnitario;
	}
}
