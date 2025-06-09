package parciales;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

public class GestionProductos {

	private ArrayList<Producto> productos = new ArrayList<Producto>();

	public void leerProductos(String archivo) throws IOException {
		FileReader fr = new FileReader(archivo);
		BufferedReader br = new BufferedReader(fr);
		String linea;
		while ((linea=br.readLine()) != null) {
			String[] datos = linea.split(",");
			try {
			this.productos.add(new Producto(datos[0], datos[1], 
					Double.parseDouble(datos[2]), Integer.parseInt(datos[3])));
			}
			catch (NumberFormatException e){
				e.printStackTrace();
				
			}
			
		}
		fr.close();
	}

	public TreeMap<String, ArrayList<Producto>> productosPorCategoria() {
		TreeMap<String, ArrayList<Producto>> ppc = new TreeMap<String, ArrayList<Producto>>();
		ArrayList<Producto> lista;
		for(Producto p : this.productos) {
			String key = p.getCategoria();
			lista = ppc.getOrDefault(key, new ArrayList<Producto>());
			lista.add(p);
			ppc.put(key, lista);
			
		}
		return ppc;

	}
	public String categoriaMasValiosa() {
		TreeMap<String, Double> ppc = new TreeMap<String, Double>();
		double valor=0;
		for(Producto p : this.productos) {
			String key = p.getCategoria();
			valor = ppc.getOrDefault(key, 0.0);
			valor += p.getPrecio()*p.getStock();
			ppc.put(key, valor);
			
		}
		Collection<Double> valores = ppc.values();
		Double max_valor = Collections.max(valores);
		
		for (Map.Entry<String, Double> entry : ppc.entrySet()) {
			String key = entry.getKey();
			Double val = entry.getValue();
			if (val == max_valor)
				return key;
		}
		return "";

	}

	public static void main(String[] args) throws IOException {
		GestionProductos gp = new GestionProductos();
		gp.leerProductos("productos.csv");
		System.out.println(gp.productosPorCategoria());
		System.out.println(gp.categoriaMasValiosa());
	}
}
