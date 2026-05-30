from prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)
        print("Libro agregado correctamente")

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        print("Usuario registrado correctamente")

    def mostrar_libros(self):
        print("\nLIBROS DISPONIBLES")
        for libro in self.__libros:
            print(f"- {libro} | Estado: {libro.estado()}")

    def mostrar_usuarios(self):
        print("\nUSUARIOS REGISTRADOS")
        for usuario in self.__usuarios:
            print(usuario)

    def realizar_prestamo(self, usuario, libro):
        if libro.prestar():
            usuario.prestar_libro(libro)
            prestamo = Prestamo(usuario, libro)
            self.__prestamos.append(prestamo)
            print("Préstamo realizado correctamente")
        else:
            print("El libro no está disponible")

    def devolver_libro(self, usuario, libro):
        libro.devolver()
        usuario.devolver_libro(libro)
        print("Libro devuelto correctamente")

    def mostrar_prestamos(self):
        print("\nPRÉSTAMOS REALIZADOS")
        for prestamo in self.__prestamos:
            print(prestamo.mostrar_prestamo())