class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__disponible = True

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def estado(self):
        if self.__disponible:
            return "Disponible"
        return "Prestado"

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}')"