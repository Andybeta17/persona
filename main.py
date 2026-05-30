from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

biblioteca = Biblioteca()

# Libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("Don Quijote", "Miguel de Cervantes")

# Usuarios
usuario1 = Usuario("Andy", 18, "2025001")
usuario2 = Usuario("Carlos", 20, "2025002")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Mostrar datos
biblioteca.mostrar_libros()
biblioteca.mostrar_usuarios()

# Realizar préstamo
biblioteca.realizar_prestamo(usuario1, libro1)

# Mostrar préstamos
biblioteca.mostrar_prestamos()

# Mostrar libros
biblioteca.mostrar_libros()

# Devolver libro
biblioteca.devolver_libro(usuario1, libro1)

# Mostrar estado final
biblioteca.mostrar_libros()