package diccionarios;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Asistencia {

	public TreeMap<String, List<String>> procesar(TreeMap<String, List<String>> entrada) {
		TreeMap<String, List<String>> salida = new TreeMap<String, List<String>>();

		for (Map.Entry<String, List<String>> entry : entrada.entrySet()) {
			String fecha = entry.getKey();
			List<String> listaDeAlumnos = entry.getValue();
			List<String> lista;
			for (String cadaAlumno : listaDeAlumnos) {
				String nuevaKey = cadaAlumno;
				if (salida.containsKey(nuevaKey)) {
					lista = salida.get(nuevaKey);
				} else {
					lista = new ArrayList<String>();
				}
				lista.add(fecha);
				salida.put(cadaAlumno, lista);
			}

		}

		return salida;
	}
	
	public static void main(String[] args) {
		TreeMap<String, List<String>> entrada = new TreeMap<String, List<String>>();
//		[(“Mie 10”: [“Ana", "Pedro"]), 
//		(“Vie 12”: [“Ana", "Luz”]), 
//		(“Mie 17”: [“Luz”, "Pedro"])]
		entrada.put("Mie 10", Arrays.asList("Ana", "Pedro", "Pepito"));
		entrada.put("Vie 12", Arrays.asList("Ana", "Luz"));
		entrada.put("Mie 17", Arrays.asList("Luz", "Pedro"));
		entrada.put("Vie 27", Arrays.asList("Pepito", "Luz", "Pedro", "Ana"));
		
		System.out.println(entrada);
		
		Asistencia as = new Asistencia();
		
		TreeMap<String, List<String>> dadaVuelta = as.procesar(entrada);
		System.out.println(dadaVuelta);
		
		/*
		 * [("Ana", [ "Mie 10", "Vie 12"]), ("Luz", [ "Vie 12", "Mie 17"] ), ("Pedro", ["Mie 10", "Mie 17"])].

		 */
		
	}

}
