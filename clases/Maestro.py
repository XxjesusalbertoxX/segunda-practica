try:
    from .Lista import Lista
except ImportError:
    from Lista import Lista

class Maestro(Lista):
    def __init__(self, id=None, nombre=None, apellido=None, edad=None, especialidad=None):
        if nombre and apellido and edad and especialidad and id:
            self.id = id
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.especialidad = especialidad
            self.lista = None
            self.es_lista = False
        else:
            super().__init__()

    def __str__(self):
        if hasattr(self, 'nombre'):
            return f"Maestro: {self.nombre} {self.apellido}, Edad: {self.edad}, Especialidad: {self.especialidad}"
        else:
            return "Numero de Maestros " + str(len(self.lista))
        
    @classmethod
    def from_dict(cls, data):
        if isinstance(data, list):
            return super().from_dict(data)
        return cls(
            id=data['id'],
            nombre=data['nombre'],
            apellido=data['apellido'],
            edad=data['edad'],
            especialidad=data.get('especialidad') or data.get('materia')
        )

if __name__ == "__main__":
    # m1 = Maestro(1, "Carlos", "Sánchez", 35, "Frances")
    # m2 = Maestro(2, "Ana", "Gómez", 30, "Física")
    # m3 = Maestro(3, "Luis", "Martínez", 40, "Química")
    # maestros = Maestro()
    # maestros.agregar(m1)
    # maestros.agregar(m2)
    # maestros.agregar(m3)
    # maestros.mostrar_uno(3)
    # maestros.mostrar()


    # maestros.guardar_en_json(r"maestros/maestros.json")

    # ##funciona por que es un metodo de clase
    # maestros_cargados = Maestro.cargar_desde_json(r"maestros/maestros.json")
    maestros2 = Maestro()
    maestros2 = Maestro.cargar_desde_json(r"maestros/maestros.json")
    maestros2.guardar_en_json(r"maestros/maestros2.json")
    # maestros2.cargar_desde_json(r"maestros/maestros2.json")
    # maestros2.mostrar()