package bebidasCalientes;

public class Cafe extends Bebida{
	private Tipo tipo;

	public Cafe(int temperatura, Tamanio volumen, Tipo tipo) {
		super(temperatura, volumen);
		this.tipo = tipo;
	}

	@Override
	public void beber() {
		System.out.println("Bebiendo un Café " + this.tipo +" " + super.toString());
		
	}

}
