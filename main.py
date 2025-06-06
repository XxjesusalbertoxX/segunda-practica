## Siguentes mejoras a realizar:
# 1. No regresar prints. unicamente booleanos pra manejar los resultados
# 2. No agregar una propiedad boleana para saber si la clase es una lista o no

from clases.Alumno import Alumno
from clases.Grupo import Grupo
from clases.Maestro import Maestro





if __name__ == "__main__":
    alumno = Alumno(1, "Juan", "Perez", 20, "123456")
    alumno2 = Alumno(2, "Ana", "Gomez", 22, "654321")
    alumno3 = Alumno(3, "Luis", "Martinez", 21, "789012")
    alumnos = Alumno()
    alumnos.agregar(alumno)
    alumnos.agregar(alumno2)
    alumnos.agregar(alumno3)
    profe1 = Maestro(1, "pendejo", "Sanchez", 35, "Matematicas")
    profe2 = Maestro(2, "Ramirez", "Gomez", 30, "Fisica")
    grupo1 = Grupo("salon C", profe1, alumnos)
    grupo2 = Grupo("manicomnio D", profe2, alumnos)
    dict_grupo = grupo1.convertir_a_diccionario()
    grupos = Grupo()
    grupos.agregar(grupo1)
    grupos.agregar(grupo2)
    grupos_dictionario = grupos.convertir_a_diccionario()
    print("Aqui va el grupo diccionario")
    print(dict_grupo)

    print("Aqui los grupos diccionario")
    print(grupos_dictionario)
    grupos.ruta = "registros/grupos.json"
    option = grupos.exportar("registros/grupos.json")
    if option:
        print("Los datos se guardaron correctamente")
    else:
        print("Error al guardar los datos")

    alumnos.ruta = "registros/alumnos.json"
    option_alumnos = alumnos.exportar("registros/alumnos.json")
    alumno.ruta = "registros/alumno.json"
    alumno.exportar("registros/alumno.json")
    if option_alumnos:
        print("Los datos de los alumnos se guardaron correctamente")
    else:
        print("Error al guardar los datos de los alumnos")

    nuevo_alumno = Alumno(4, "Maria", "Lopez", 19, "345678")
    nuevo_alumno.importar("registros/alumno.json")
    print("El nuevo alumno es")
    print(nuevo_alumno)
    nuevos_alumnos = Alumno()
    nuevos_alumnos.importar("registros/alumnos.json")
    print("Los nuevos alunos son")
    print(nuevos_alumnos)



    """
    alumno = Alumno(1,"Juan", "Pérez", 20, "123456")
    alumno2 = Alumno(2,"Ana", "Gómez", 22, "654321")
    alumno3 = Alumno(3,"Luis", "Martínez", 21, "789012")
    alumnos = Alumno()
    alumnos.agregar(alumno)
    alumnos.agregar(alumno2)
    alumnos.agregar(alumno3)
    alumnos.mostrar_uno(3)


    alumno.mostrar()
    alumnos.mostrar()
    alumnos_diccionario = alumnos.convertir_a_diccionario()
    print("Aqui va el alumno diccionario ")
    print(alumnos_diccionario)


    alumnos.eliminar(2)

    print("aqui elimino un alimno")

    diccionario2 = alumnos.convertir_a_diccionario()

    print(diccionario2)


    alumnos.mostrar()
    """

