package bebidasCalientes;

public class Te extends Bebida {
	private Variedad variedad;

	public Te(int temperatura, Tamanio volumen, Variedad variedad) {
		super(temperatura, volumen);
		this.variedad = variedad;
	}

	@Override
	public void beber() {
		System.out.println("Bebiendo un Té " + this.variedad +" " + super.toString());
		
	}

}
