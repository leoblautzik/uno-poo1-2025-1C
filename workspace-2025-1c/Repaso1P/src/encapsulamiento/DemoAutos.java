package encapsulamiento;

import java.util.ArrayList;

public class DemoAutos {

	public static void main(String[] args) {
		
		ArrayList<Auto> autos = new ArrayList<Auto>();
		autos.add(new Auto("Renault", "naftero"));
		autos.add(new Auto("Tesla", "electrico"));
		
		for(Auto cadaAuto : autos) {
			System.out.println(cadaAuto);
		}
	}

}
