package bebidasCalientes;

import java.util.ArrayList;

public abstract  class Bebida {
	private int temperatura;
	private Tamanio volumen;
	
	public Bebida(int temperatura, Tamanio volumen) {
		this.temperatura = temperatura;
		this.volumen = volumen;
	}
	
	public abstract void beber();
	
	@Override
	public String toString() {
		return "a "+ temperatura + "°C"+ " de tamaño " + volumen;
	}
	
	public static void main(String[] args) {
		
		Cafe cafecito = new Cafe(80, Tamanio.MEDIANO, Tipo.expreso);
		Te tecito = new Te(90, Tamanio.GRANDE,  Variedad.negro);
		ChocolateCaliente choco = new ChocolateCaliente(85, true);
		ChocolateCaliente chocosolo = new ChocolateCaliente(85, false);
		
		ArrayList<Bebida> bebidas = new ArrayList<Bebida>();
		bebidas.add(tecito);
		bebidas.add(cafecito);
		bebidas.add(chocosolo);
		bebidas.add(choco);
		
		for(Bebida cadaUna : bebidas) {
			cadaUna.beber();
		}
		
	}
	
	
	

}
