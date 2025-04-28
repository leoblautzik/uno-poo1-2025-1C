package profesionales;

import java.util.ArrayList;
import java.util.Collections;

public class Demo {

	public static void main(String[] args) {
		Medico juancito = new Medico("Juan", "Perez");
		Cirujano luisito = new Cirujano("Luis", "Luque");
		CirujanoCardiovascular benito= new CirujanoCardiovascular("Benito", "Juarez");
		Dentista silvia = new Dentista("Silvia", "Perez");
		Endodoncista endo = new Endodoncista("Javier", "Lopez");
		
		ArrayList<Profesional> profesionales = new ArrayList<Profesional>();
		profesionales.add(juancito);
		profesionales.add(luisito);
		profesionales.add(benito);
		profesionales.add(silvia);
		profesionales.add(endo);
		
		Profesional.setHonorarioBasico(1300000);
		Collections.sort(profesionales);
		
		for(Profesional p : profesionales) {
			System.out.println(p);
		}

	}

}
