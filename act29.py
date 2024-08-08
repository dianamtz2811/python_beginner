#Crea una clase Libro con atributos de instancia como titulo, autor, año_publicacion, y disponible (un valor booleano que indica si el libro está disponible o no). Luego, crea una clase Biblioteca que tenga una lista de libros y métodos de instancia para prestar un libro, devolver un libro y mostrar todos los libros disponibles. Utiliza atributos de clase para registrar la cantidad total de libros en la biblioteca. Crea instancias de ambas clases y realiza operaciones de préstamo y devolución de libros.
#Para modificar un atributo de clase podes hacer lo siguiente:
#Casa.atributo_de_clase = ‘prueba’
#En este ejemplo se toma Casa como la clase y el atributo atributo_de_clase, donde se guarda un string (esto puede hacerse desde los metodos.

class Libro:
    def __init__(self, titulo, autor, anyo_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anyo_publicacion = anyo_publicacion
        self.disponible = True

class Biblioteca:
    cantidad_total_libros = 0

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        Biblioteca.cantidad_total_libros += 1

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.disponible = False
                return f"El libro '{titulo}' ha sido prestado."
        return f"El libro '{titulo}' no está disponible."

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and not libro.disponible:
                libro.disponible = True
                return f"El libro '{titulo}' ha sido devuelto."
        return f"El libro '{titulo}' no puede ser devuelto."

    def mostrar_libros_disponibles(self):
        disponibles = [libro.titulo for libro in self.libros if libro.disponible]
        return f"Libros disponibles: {', '.join(disponibles)}"

#Instanciando objetos
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "1985")
libro2 = Libro("En busca del tiempo perdido", "Marcel Proust", "1899")

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print(biblioteca.prestar_libro("Cien años de soledad"))
print(biblioteca.devolver_libro("Cien años de soledad"))
print(biblioteca.mostrar_libros_disponibles()) 