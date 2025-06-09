try:
    from .Lista import Lista
    from .Alumno import Alumno
    from .Maestro import Maestro
except ImportError:
    from Lista import Lista
    from Alumno import Alumno
    from Maestro import Maestro

class Grupo(Lista):
    def __init__(self, Nombre=None, Maestro=None, Alumnos=None):
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
            return f"Grupo: {self.Nombre}, Maestro: {self.Maestro}, Alumnos: {self.Alumnos}"
        else:
            return "Numero de Grupos " + str(len(self.lista))
        
    @classmethod
    def from_dict(cls, data):
        if isinstance(data, list):
            return super().from_dict(data)
        maestro = Maestro.from_dict(data['Maestro'])
        alumnos = Alumno()
        for alumno_dict in data['Alumnos']:
            alumnos.agregar(Alumno.from_dict(alumno_dict))
        return cls(data['Nombre'], maestro, alumnos)

if __name__ == "__main__":
    
    maestro1 = Maestro(1, "Carlos", "Sánchez", 35, "Matemáticas")
    maestro2 = Maestro(1, "Juanito", "sola", 35, "Español")
    maestro3 = Maestro(1, "Carlos", "Pedro", 35, "Ingles")
    a1 = Alumno(1, "Juan", "Pérez", 20, "123456")
    a2 = Alumno(2, "Ana", "Gómez", 22, "654321")
    a3 = Alumno(3, "Luis", "Martínez", 21, "789012")

    alumnos = Alumno()
    alumnos.agregar(a1)
    alumnos.agregar(a2)
    alumnos.agregar(a3)
    g1 = Grupo("Grupo A", maestro1, alumnos)
    g2 = Grupo("Grupo B", maestro2, alumnos)
    
    
    grupos = Grupo()    ##grupos.mostrar()
    grupos.agregar(g1)
    grupos.agregar(g2)

    grupo = Grupo.cargar_desde_json(r"grupos/grupos.json")
    grupo.guardar_en_json(r"grupos/unonuevo.json")
    
    
    # grpos = Grupo()
    # grpos = Grupo.cargar_desde_json(r"grupos/grupowardadonuevo2.json")
    # grpos.mostrar()

    
    # grupos_cargados.guardar_en_json(r"grupos/grupos2.json")
    # grupos_cargados.cargar_desde_json(r"grupos/grupos2.json")
    # grupos_cargados.guardar_en_json(r"grupos/grupos3.json")
    # grupos_cargados.cargar_desde_json(r"grupos/grupos3.json")
    # grupos_cargados.mostrar()
