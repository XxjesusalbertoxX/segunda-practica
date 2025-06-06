try:
    from .Lista import Lista
except ImportError:
    from Lista import Lista

class Alumno(Lista):
    def __init__(self,id = None, nombre=None, apellido=None, edad=None, matricula=None):
        if nombre and apellido and edad and matricula and id:
            self.id = id
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.matricula = matricula
            self.lista = None
            self.es_lista = False
        else:
            super().__init__()


    def __str__(self):
        if hasattr(self, 'nombre'):
            return f"Alumno: {self.nombre} {self.apellido}, Edad: {self.edad}, Matrícula: {self.matricula}"
        else:
            return "Numero de Alumnos " + str(len(self.lista))
    
    @classmethod
    def from_dict(cls, data):
        # Si recibe una lista, delega a la clase base
        if isinstance(data, list):
            return super().from_dict(data)
        # Si recibe un diccionario, crea un Alumno
        return cls(
            id=data['id'],
            nombre=data['nombre'],
            apellido=data['apellido'],
            edad=data['edad'],
            matricula=data['matricula']
        )
    
            
if __name__ == "__main__":
    # a1 = Alumno(1,"Juan", "Pérez", 20, "123456")
    # a2 = Alumno(2,"Ana", "Gómez", 22, "654321")
    # a3 = Alumno(3,"Luis", "Martínez", 21, "789012")
    # alumnos = Alumno()
    # alumnos.agregar(a1)
    # alumnos.agregar(a2)
    # alumnos.agregar(a3)
    # a1.mostrar()

    alumnos2 = Alumno()
    alumnos2 = alumnos2.cargar_desde_json(r"alumnos/alumnos.json")
    a1 = Alumno(4,"Juan", "Pérez", 20, "123456")
    alumnos2.agregar(a1)


    alumnos2.guardar_en_json(r"alumnos/alumnos.json")
    # alumnos2.mostrar()
    ## alumnos.mostrar()