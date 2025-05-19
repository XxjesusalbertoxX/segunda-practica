from .Lista import Lista
from .Alumno import Alumno
from .Maestro import Maestro

class Grupo(Lista):
    def __init__(self, Nombre = None, Maestro = None, Alumnos=None):
        if Nombre and Maestro and Alumnos:
            self.Nombre = Nombre
            self.Maestro = Maestro
            self.Alumnos = Alumnos
            self.lista = None
            self.es_lista = False
        else:
            super().__init__()

    def __str__(self):
        if hasattr(self, 'Nombre'):
            return f"(Grupo: {self.Nombre}), (Maestro: {self.Maestro}), (Alumnos: {self.Alumnos})"
        else:
            return "Numero de Grupos " + str(len(self.lista))



if __name__ == "__main__":
    maestro1 = Maestro(1, "Carlos", "Sánchez", 35, "Matemáticas")
    alumno1 = Alumno(1, "Juan", "Pérez", 20, "123456")
    alumno2 = Alumno(2, "Ana", "Gómez", 22, "654321")
    alumno3 = Alumno(3, "Luis", "Martínez", 21, "789012")

    alumnos = Alumno()
    alumnos.agregar(alumno1)
    alumnos.agregar(alumno2)
    alumnos.agregar(alumno3)
    grupo = Grupo("Grupo A", maestro1, alumnos)
    grupo2 = Grupo("Grupo B", maestro1, alumnos)
    grupos = Grupo()
    grupos.agregar(grupo)
    grupos.agregar(grupo2)
    grupo.mostrar()
    grupos.mostrar()