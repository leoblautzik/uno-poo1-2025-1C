package restaurante;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

public class Restaurante {

	private TreeMap<Integer, List<Consumo>> mesas;

	public Restaurante() {
		this.mesas = new TreeMap<Integer, List<Consumo>>();
	}

	public void agregarConsumo(int mesa, Consumo c) {
		List<Consumo> lista;
		if (mesas.containsKey(mesa)) {
			lista = mesas.get(mesa);
		} else {
			lista = new ArrayList<Consumo>();
		}
		lista.add(c);
		mesas.put(mesa, lista);

	}

	public String ticket(int mesa) {
		String t = "Consumos de la mesa " + mesa + "\n";
		double total = 0;
		List<Consumo> listaDeConsumos = mesas.get(mesa);

		for (Consumo c : listaDeConsumos) {
			total += c.getPrecio();
			t += c.toString();
			t += "\n";
		}
		t += "Total: " + total;

		return t;

	}

	public static void main(String[] args) {
		Restaurante loDePipo = new Restaurante();
		loDePipo.agregarConsumo(100, new Consumo(1, "Coca", 2000));
		loDePipo.agregarConsumo(200, new Consumo(5, "Cafe con leche + 3", 4000));
		loDePipo.agregarConsumo(100, new Consumo(2, "Pancho", 1500));
		loDePipo.agregarConsumo(200, new Consumo(3, "Cafe cortado", 2500));
		System.out.println(loDePipo.ticket(100));
		System.out.println(loDePipo.ticket(200));

	}

}
