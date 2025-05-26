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

    def convertir_json_objeto(self, data):
        if self.es_lista:
            self.lista = []
            for item in data:
                nuevo_grupo=Grupo()
                nuevo_grupo.es_lista = False
                nuevo_grupo=nuevo_grupo.convertir_json_objeto(item)
                self.lista.append(nuevo_grupo)
        else:

            self.Nombre = data.get('Nombre')

            maestro_dict = data.get('Maestro', {})
            if not hasattr(self, 'Maestro'):
                self.Maestro = Maestro()
                self.Maestro.es_lista = False
                self.Maestro.convertir_json_objeto(maestro_dict)

            alumnos_lista = Alumno()
            alumnos_lista.es_lista = True
            alumnos_lista.convertir_json_objeto(data.get('Alumnos', []))
            self.Alumnos = alumnos_lista
            grup = Grupo(self.Nombre, self.Maestro, self.Alumnos)
            return grup




    def convertir_a_diccionario(self):
        if self.lista:
            grupos_diccionario = []
            for item in self.lista:
                print(item)
                grupos_diccionario.append(item.convertir_a_diccionario())
            return grupos_diccionario

        else:
            alumnos_diccionario = self.Alumnos.convertir_a_diccionario()
            return {
                "Nombre": self.Nombre,
                "Maestro": vars(self.Maestro),
                "Alumnos": alumnos_diccionario
            }



if __name__ == "__main__":
    """
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

    grupo.exportar("registros/grupo1.json")
    grupos.exportar("registros/grupos1.json")

    nuevo_grupo = Grupo("Grupo Z", maestro1, alumnos)
    nuevo_grupo.importar("registros/grupo1.json")
    """
    nuevos_grupos = Grupo()
    nuevos_grupos.importar("registros/grupos1.json")
    print("El nuevo grupo es")
    print("Los nuevos grupos son")
    nuevos_grupos.mostrar()

    nuevos_grupos.exportar("registros/grupooooooos.json")
