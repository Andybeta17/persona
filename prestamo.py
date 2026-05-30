from datetime import datetime

class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha = datetime.now()

    def mostrar_prestamo(self):
        return f"{self.usuario.nombre} prestó '{self.libro.titulo}' el {self.fecha.strftime('%d/%m/%Y')}"