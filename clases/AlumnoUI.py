import os
from AlumnoClass import Alumno

class AlumnoUI:
    def __init__(self,alumnos=None):
        self.path = 'alumnos/alumnos.json'

        self.guardar_json = alumnos is None

        if self.guardar_json:
            self.alumnos = Alumno.cargar_desde_json(self.path)
        else:
            self.alumnos = alumnos


    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu_alumnos(self):
        while True:
            self.clear()
            print("--- Gestión de Alumnos ---")
            print("1. Agregar alumno")
            print("2. Listar alumnos")
            print("3. Editar")
            print("4. Eliminar alumno por ID")
            print("0. Volver")
            choice = input("Opción: ")
            if choice == '1':
                self.agregar_alumno()
            elif choice == '2':
                self.listar_alumnos()
            elif choice == '3':
                self.editar_alumno()
            elif choice == '4':
                self.eliminar_alumno()
            elif choice == '0':
                break
            else:
                print("Opción no válida.")
            input("Presiona Enter para continuar...")

        return self.alumnos
    
    def editar_alumno(self):
        try:
            id_to_edit = int(input("ID del alumno a editar: "))
        except ValueError:##detiene la exception
            print("ID inválido.")
            return

        ## buscamos el alumno existente recorriendo la lista y comparando el id
        existing = None
        for p in self.alumnos.lista:
            if p.id == id_to_edit:
                existing = p
                break

        if not existing:##regreso si no se encuentra
            print(f"No existe ningún alumno con ID {id_to_edit}.")
            return

        ##pedirmos los datos y si no coloca nada lo dejamos igual
        nombre   = input(f"Nombre [{existing.nombre}]: ") or existing.nombre
        apellido = input(f"Apellido [{existing.apellido}]: ") or existing.apellido
        edad_str = input(f"Edad [{existing.edad}]: ")
        matricula= input(f"Matrícula [{existing.matricula}]: ") or existing.matricula

        try:## un try para por si la edad es string 
            edad = int(edad_str) if edad_str else existing.edad
        except ValueError:
            print("Edad inválida, se mantiene la anterior.")
            edad = existing.edad

        ## se actualiza la nueva informacion
        updated = Alumno(
            id=id_to_edit,
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            matricula=matricula
        )

        # ya solo llamamos la funcion de editar para que lo inserte de forma correcta
        if self.alumnos.editar(id_to_edit, updated):
            if not self.guardar_json:
                self.alumnos.guardar_en_json(self.path) ## se guarda automatico en el json
            print("Alumno editado correctamente.")
        else:
            print("Error al editar el alumno.")

        

    def agregar_alumno(self):
        id = int(input("ID del alumno: "))
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        matricula = input("Matrícula: ")
        print("Datos inválidos.")

        nuevo = Alumno(id, nombre, apellido, edad, matricula)
        self.alumnos.agregar(nuevo)

        if not self.guardar_json:
            self.alumnos.guardar_en_json(self.path)

        print("Alumno agregado.")

    def listar_alumnos(self):
        self.alumnos.mostrar()

    def eliminar_alumno(self):
        id_borrar = input("Ingrese el ID del alumno a eliminar: ")
        if id_borrar.isdigit():
            self.alumnos.eliminar(int(id_borrar))
            if not self.guardar_json:
                self.alumnos.guardar_en_json(self.path)
            print("Alumno eliminado.")
        else:
            print("ID inválido.")

if __name__ == "__main__":
    alumno_ui = AlumnoUI()
    alumno_ui.menu_alumnos()
