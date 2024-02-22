class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)

# Creación de instancias de Libro
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien")
libro2 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling")

# Creación de una instancia de Biblioteca y agregación de libros
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Mostrar libros en la biblioteca
biblioteca.mostrar_libros()
