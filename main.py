## Siguentes mejoras a realizar:
# 1. No regresar prints. unicamente booleanos pra manejar los resultados
# 2. No agregar una propiedad boleana para saber si la clase es una lista o no

from clases.Alumno import Alumno


if __name__ == "__main__":
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