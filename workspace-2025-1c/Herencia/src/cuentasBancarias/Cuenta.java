package cuentasBancarias;

public abstract class Cuenta {
	
	private int dni;
	private double saldo =0;
	
	public Cuenta(int dni) {
		this.dni=dni;
	}
	
	public void depositar(double monto) {
		this.saldo+=monto;
	}
	
	public double extraer(double monto) {
		if(monto > this.saldo) {
			throw new Error("No alcanza");
		}
		this.saldo-= monto;
		return monto;
	}

}
