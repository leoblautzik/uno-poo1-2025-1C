package bebidasCalientes;

public class ChocolateCaliente extends Bebida {

	private boolean marshmallows;

	public ChocolateCaliente(int temperatura, boolean marshmallows) {
		super(temperatura, Tamanio.GRANDE);
		this.marshmallows = marshmallows;
	}

	@Override
	public void beber() {
		if (this.marshmallows) {
			System.out.println("Bebiendo un Chocolate con marshmallows " + super.toString());
		} else {
			System.out.println("Bebiendo un Chocolate solo " + super.toString());

		}
	}
}
