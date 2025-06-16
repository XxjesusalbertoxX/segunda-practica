# Grupo.py
try:
    from .Lista import Lista
    from .AlumnoClass import Alumno
    from .MaestroClass import Maestro
except ImportError:
    from Lista import Lista
    from AlumnoClass import Alumno
    from MaestroClass import Maestro

class Grupo(Lista):
    def __init__(self, id=None, nombre=None, grado=None, seccion=None, maestro=None, alumnos=None, turno=None):
        if nombre is not None and maestro is not None and alumnos is not None:
            self.id       = id
            self.nombre   = nombre
            self.grado    = grado
            self.seccion  = seccion
            self.maestro  = maestro    # instancia de Maestro
            self.alumnos  = alumnos    # instancia de Alumno (contenedor)
            self.turno    = turno
            self.es_lista = False
            self.lista    = None
        else:
            super().__init__()

    def __str__(self):
        if not self.es_lista:
            alumnos_str = ', '.join(str(a) for a in self.alumnos.lista)
            return (f"Grupo {self.id}: {self.nombre} (Grado {self.grado}, Sección {self.seccion})\n"
                    f"  Maestro: {self.maestro}\n"
                    f"  Alumnos: {alumnos_str}\n"
                    f"  Turno: {self.turno}")
        return f"Número de grupos: {len(self.lista)}"

    @classmethod
    def from_dict(cls, data):
        # data es un dict con claves: 'id','nombre','grado','seccion','maestro','alumnos','turno'
        maestro = Maestro.from_dict(data['maestro'])
        cont_al = Alumno() 
        for ad in data['alumnos']:
            cont_al.agregar(Alumno.from_dict(ad))
        return cls(
            id      = data['id'],
            nombre  = data['nombre'],
            grado   = data['grado'],
            seccion = data['seccion'],
            maestro = maestro,
            alumnos = cont_al,
            turno   = data.get('turno')
        )
    
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
    g1 = Grupo(2, "Grupo A", "4" , "C" , maestro1, alumnos, "vespertino")
    # g2 = Grupo(4, "Grupo B", "2" , "A" ,  maestro2, alumnos, "nocturno")
    
    
    grupos = Grupo()    ##grupos.mostrar()
    grupos.agregar(g1)

    grupos.guardar_en_json(r"grupos/grupos.json")
    grupo = Grupo.cargar_desde_json(r"grupos/grupos.json")