d(libro)

    def devolver_libro(self, libro):from persona import Persona

class Usuario(Persona):
    def __init__(self, nombre, edad, carnet):
        super().__init__(nombre, edad)
        self.carnet = carnet
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.appen
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre} - Carnet: {self.carnet}"