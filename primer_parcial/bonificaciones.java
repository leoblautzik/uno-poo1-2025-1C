// Java - Sistema de Empleados

abstract class Empleado {
    protected String nombre;
    protected double salarioBase;
    protected String dni;

    public Empleado(String nombre, double salarioBase, String dni) {
        this.nombre = nombre;
        this.salarioBase = salarioBase;
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public double getSalario() {
        return salarioBase;
    }

    public abstract double calcularBonificacion();
}

class Gerente extends Empleado {
    public Gerente(String nombre, double salarioBase, String dni) {
        super(nombre, salarioBase, dni);
    }

    @Override
    public double calcularBonificacion() {
        return salarioBase * 0.10;
    }
}

class Desarrollador extends Empleado {
    public Desarrollador(String nombre, double salarioBase, String dni) {
        super(nombre, salarioBase, dni);
    }

    @Override
    public double calcularBonificacion() {
        return salarioBase * 0.07;
    }
}

public class Empresa {
    public static void mostrarBonificaciones(Empleado[] empleados) {
        for (Empleado e : empleados) {
            System.out.println("Nombre: " + e.getNombre() + " - Bonificaci\u00f3n: $" + e.calcularBonificacion());
        }
    }

    public static void main(String[] args) {
        Empleado[] empleados = {
            new Gerente("Ana Torres", 50000, "12345678"),
            new Desarrollador("Luis G\u00f3mez", 100000, "23456789"),
            new Empleado("Marta Ruiz", 70000, "34567890") {
                @Override
                public double calcularBonificacion() {
                    return salarioBase * 0.05;
                }
            }
        };

        mostrarBonificaciones(empleados);
    }
}

