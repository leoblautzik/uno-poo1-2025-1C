package io;

import java.util.Objects;

public class Punto {
	private double x;
	private double y;
	
	public Punto(double x, double y) {
		this.x = x;
		this.y = y;
	}

	public double getX() {
		return x;
	}

	public double getY() {
		return y;
	}

	@Override
	public String toString() {
		return "(" + x + ", " + y + ")";
	}
	
	
	
	@Override
	public int hashCode() {
		return Objects.hash(x, y);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Punto other = (Punto) obj;
		return Double.doubleToLongBits(x) == Double.doubleToLongBits(other.x)
				&& Double.doubleToLongBits(y) == Double.doubleToLongBits(other.y);
	}

	public static void main(String[] args) {
		Punto p1 = new Punto(1,1);
		Punto otroP1 = p1;
		System.out.println(otroP1 == p1);
		Punto p2 = new Punto(2,4);
		Punto p3 = new Punto(1,1);
		System.out.println(p1==p2);
		System.out.println(p1==p3);
		
		System.out.println(p1.equals(p3));
		
		System.out.println("Hola".equals(new String("Hola")));
		System.out.println(0.1 + 0.2);
		
		
	}
	
	
	
	
	
	

}
