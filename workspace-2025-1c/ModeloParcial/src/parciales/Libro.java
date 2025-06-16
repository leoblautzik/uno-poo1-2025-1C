package parciales;

public class Libro {
    private String titulo;
    private String autor;
    private String genero;
    private int cantidadDisponible;

    public Libro(String titulo, String autor, String genero, int cantidadDisponible) {
        this.titulo = titulo;
        this.autor = autor;
        this.genero = genero;
        this.cantidadDisponible = cantidadDisponible;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public String getGenero() {
        return genero;
    }

    public int getCantidadDisponible() {
        return cantidadDisponible;
    }

    @Override
    public String toString() {
        return titulo + ", " + autor + ", " + genero + ", " + cantidadDisponible;
    }
}

