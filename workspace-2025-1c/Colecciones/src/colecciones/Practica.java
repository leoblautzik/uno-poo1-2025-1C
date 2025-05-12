package colecciones;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class Practica {

	public LinkedList<Integer> eliminarDuplicados(List<Integer> enteros) {
		LinkedList<Integer> aux = new LinkedList<Integer>();
		for (Integer cadaUno : enteros) {
			if (!aux.contains(cadaUno)) {
				aux.add(cadaUno);
			}
		}

		return aux;
	}

	public LinkedList<Integer> invertirLista(List<Integer> enteros) {
		LinkedList<Integer> aux = new LinkedList<Integer>();
		for (Integer cadaUno : enteros) {

			aux.addFirst(cadaUno);
		}

		return aux;
	}

	public boolean esSublista(List<Integer> l1, List<Integer> l2) {
		for (int i = 0; i < l2.size() - l1.size() + 1; i++) {
			if (l2.subList(i, i + l1.size()).equals(l1))
				return true;
		}
		return false;

	}

	public String terminalDeTeletipo(String cadena) {
		Stack<Character> aux = new Stack<Character>();
		Stack<Character> aux2 = new Stack<Character>();
		String s = "";
		for (Character c : cadena.toCharArray()) {
			if (c != '/' && c != '&') {
				aux.push(c);
			} else if (c == '/') {
				if (!aux.empty())
					aux.pop();
			} else if (c == '&') {
				aux.clear();
			}

		}
		while (!aux.empty()) {
			aux2.push(aux.pop());
		}

		while (!aux2.empty()) {
			s += aux2.pop();
		}

		return s;

	}

	public static void main(String[] args) {
		ArrayList<Integer> l1 = new ArrayList<Integer>();
		l1.add(1);
		l1.add(2);
		l1.add(2);
		l1.add(4);
		l1.add(2);
		l1.add(1);
		l1.add(5);

		Practica p1 = new Practica();
		System.out.println(p1.eliminarDuplicados(l1));
		System.out.println(p1.invertirLista(l1));

	}
}
