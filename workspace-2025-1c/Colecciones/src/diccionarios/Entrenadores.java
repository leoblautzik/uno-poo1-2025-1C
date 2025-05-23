package diccionarios;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;


public class Entrenadores {
	
	public TreeMap<String, TreeSet<String>> procesar(HashMap<String, List<String>> entrada) {
		TreeMap<String, TreeSet<String>> salida = new TreeMap<String, TreeSet<String>>();
		
		for (Map.Entry<String, List<String>> entry : entrada.entrySet()) {
			String entrenador = entry.getKey();
			List<String> listaDeSocios = entry.getValue();
			TreeSet<String> listaDeEntrenadores;
			for(String socio : listaDeSocios) {
				listaDeEntrenadores = salida.getOrDefault(socio, new TreeSet<String>());
//				if(salida.containsKey(socio)) {
//					listaDeEntrenadores = salida.get(socio);
//				}
//				else {
//					listaDeEntrenadores = new TreeSet<String>();
//				}
				listaDeEntrenadores.add(entrenador);
				salida.put(socio, listaDeEntrenadores);
			}
		}
		
		return salida;
	}

	public static void main(String[] args) {
		/*
		 * “Bielsa” contiene la lista [“Juan”, “Alberto”], 
		 * y en la clave “Alvarez” contiene la lista [“Tom”, “Alberto”, “Vero”], 
		*/
		
		Entrenadores en = new Entrenadores();
		HashMap<String, List<String>> entrenadores = new HashMap<String, List<String>>();
		entrenadores.put("Bielsa", Arrays.asList("Juan", "Alberto", "Fabra"));
		entrenadores.put("Alvarez", Arrays.asList("Tom", "Alberto", "Vero"));
		entrenadores.put("Gago", Arrays.asList("Rojo", "Fabra", "Benedetto"));
		entrenadores.put("Gago", Arrays.asList("Merentiel", "Fabra", "Benedetto"));
		
		System.out.println(entrenadores);
		
		System.out.println(en.procesar(entrenadores));
		
		

	}

}
