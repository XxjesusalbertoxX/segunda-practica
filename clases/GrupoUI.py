import os
from Grupo import Grupo
from MaestroClass import Maestro
from AlumnoClass import Alumno
from MaestroUI import MaestroUI

class GrupoUI:
    def __init__(self, is_object=False):
        self.path = 'grupos/grupos.json'
        self.is_object = is_object

        if self.is_object:
            self.grupos = Grupo()
        else:
            self.grupos = Grupo.cargar_desde_json(self.path)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu_grupos(self):
        while True:
            self.clear()
            print("--- Gestión de Grupos ---")
            print("1. Agregar grupo")
            print("2. Listar grupos")
            print("3. Editar grupo")
            print("4. Eliminar grupo por ID")
            print("0. Volver")
            choice = input("Opción: ")
            if choice == '1':
                self.agregar_grupo()
            elif choice == '2':
                self.listar_grupos()
            elif choice == '3':
                self.editar_grupo()
            elif choice == '4':
                self.eliminar_grupo()
            elif choice == '0':
                break
            else:
                print("Opción no válida.")
            input("Presiona Enter para continuar...")

        return self.grupos

    def agregar_grupo(self):
        id_grupo = int(input("ID del grupo: "))
        nombre = input("Nombre del grupo: ")
        grado = input("Grado: ")
        seccion = input("Sección: ")
        turno = input("Turno: ")

        print("--- Datos del maestro ---")
        id_m = int(input("ID maestro: "))
        nombre_m = input("Nombre maestro: ")
        apellido_m = input("Apellido maestro: ")
        edad_m = int(input("Edad maestro: "))
        materia = input("Materia: ")
        maestro = Maestro(id_m, nombre_m, apellido_m, edad_m, materia)

        alumnos = Alumno()
        while True:
            print("Agregar alumno:")
            id_a = int(input("ID alumno: "))
            nombre_a = input("Nombre: ")
            apellido_a = input("Apellido: ")
            edad_a = int(input("Edad: "))
            matricula = input("Matrícula: ")
            alumnos.agregar(Alumno(id_a, nombre_a, apellido_a, edad_a, matricula))

            otro = input("¿Agregar otro alumno? (s/n): ").lower()
            if otro != 's':
                break

        nuevo_grupo = Grupo(id_grupo, nombre, grado, seccion, maestro, alumnos, turno)
        self.grupos.agregar(nuevo_grupo)

        if not self.is_object:
            self.grupos.guardar_en_json(self.path)

        print("Grupo agregado correctamente.")

    def listar_grupos(self):
        self.grupos.mostrar()

    def editar_grupo(self):
        try:
            id_edit = int(input("ID del grupo a editar: "))
        except ValueError:
            print("ID inválido.")
            return

        existente = None
        # Convertimos g.id a entero para comparar con id_edit
        for g in self.grupos.lista:
            try:
                if int(g.id) == id_edit:
                    existente = g
                    break
            except (ValueError, TypeError):
                continue

        if not existente:
            print(self.grupos.lista)  # para debug
            print(f"No existe ningún grupo con ID {id_edit}.")
            return

        # Pedimos datos generales
        nombre  = input(f"Nombre [{existente.nombre}]: ")  or existente.nombre
        grado   = input(f"Grado [{existente.grado}]: ")    or existente.grado
        seccion = input(f"Sección [{existente.seccion}]: ") or existente.seccion
        turno   = input(f"Turno [{existente.turno}]: ")    or existente.turno

        # ¿Editar maestro?
        if input("¿Editar maestro? (s/n): ").lower() == 's':
            m_ui = MaestroUI(is_object=True)

            contenedor_maestros = Maestro()
            contenedor_maestros.agregar(existente.maestro)

            m_ui.maestros = contenedor_maestros
            nuevo_maestro = m_ui.editar_maestro()  # Debe devolver un objeto tipo Maestro
        else:
            nuevo_maestro = existente.maestro

        # ¿Editar alumnos?
        if input("¿Editar alumnos? (s/n): ").lower() == 's':
            from AlumnoUI import AlumnoUI
            a_ui = AlumnoUI(is_object=True)
            # Pre-cargamos la lista de alumnos actual
            a_ui.alumnos = existente.alumnos  
            # menu_alumnos() retorna el contenedor Alumno con .lista actualizado
            nuevos_alumnos = a_ui.menu_alumnos()
        else:
            nuevos_alumnos = existente.alumnos

        # Creamos la instancia actualizada
        grupo_editado = Grupo(
            id      = existente.id,
            nombre  = nombre,
            grado   = grado,
            seccion = seccion,
            maestro = nuevo_maestro,
            alumnos = nuevos_alumnos,
            turno   = turno
        )

        # Reemplazamos en la lista
        if self.grupos.editar(id_edit, grupo_editado):
            if not self.is_object:
                self.grupos.guardar_en_json(self.path)
            print("Grupo editado correctamente.")
        else:
            print("Error al editar el grupo.")


    def eliminar_grupo(self):
        id_borrar = input("Ingrese el ID del grupo a eliminar: ")
        if id_borrar.isdigit():
            self.grupos.eliminar(int(id_borrar))
            if not self.is_object:
                self.grupos.guardar_en_json(self.path)
            print("Grupo eliminado.")
        else:
            print("ID inválido.")

if __name__ == "__main__":
    grupo_ui = GrupoUI()
    grupo_ui.menu_grupos()
