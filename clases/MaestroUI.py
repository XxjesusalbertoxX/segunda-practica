import os
from MaestroClass import Maestro

class MaestroUI:
    def __init__(self, is_object=False):
        self.path = 'maestros/maestros.json'
        self.is_object = is_object
        # Carga inicial según bandera
        if self.is_object:
            self.maestros = Maestro()
        else:
            self.maestros = Maestro.cargar_desde_json(self.path)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu_maestros(self):
        """
        Muestra el menú de gestión de maestros.
        Al salir, siempre devuelve la instancia de Maestro en uso.
        """
        while True:
            self.clear()
            print("--- Gestión de Maestros ---")
            print("1. Agregar maestro")
            print("2. Listar maestros")
            print("3. Editar maestro")
            print("4. Eliminar maestro por ID")
            print("0. Salir")
            choice = input("Opción: ")

            if choice == '1':
                self.agregar_maestro()
            elif choice == '2':
                self.listar_maestros()
            elif choice == '3':
                self.editar_maestro()
            elif choice == '4':
                self.eliminar_maestro()
            elif choice == '0':
                break
            else:
                print("Opción no válida.")
            input("Presiona Enter para continuar...")

        # Al salir del menú, regresamos el objeto Maestro
        return self.maestros

    def agregar_maestro(self):
        """
        Crea un nuevo maestro y lo agrega al objeto.
        """
        # Se crea un nuevo Maestro usando su constructor
        nuevo = self._pedir_datos_maestro()
        self.maestros.agregar(nuevo)
        # Solo guardamos a JSON si no venimos como objeto en memoria
        if not self.is_object:
            self.maestros.guardar_en_json(self.path)
        print("Maestro agregado")

    def listar_maestros(self):
        """Imprime la lista completa de maestros."""
        self.maestros.mostrar()

    def eliminar_maestro(self):
        """Elimina un maestro por su ID."""
        id_borrar = input("Ingrese el ID del maestro a eliminar: ")
        eliminado = self.maestros.eliminar(id_borrar)
        if eliminado:
            if not self.is_object:
                self.maestros.guardar_en_json(self.path)
            print(f"Maestro con ID {id_borrar} eliminado.")
        else:
            print(f"No se encontró ningún maestro con ID {id_borrar}.")

    def editar_maestro(self):
        try:
            id_to_edit = int(input("ID del maestro a editar: "))
        except ValueError:##detiene la exception
            print("ID inválido.")
            return

        ## buscamos el alumno existente recorriendo la lista y comparando el id
        existing = None
        for p in self.maestros.lista:
            if p.id == id_to_edit:
                existing = p
                break

        if not existing:##regreso si no se encuentra
            print(f"No existe ningún maestros con ID {id_to_edit}.")
            return

        ##pedirmos los datos y si no coloca nada lo dejamos igual
        nombre   = input(f"Nombre [{existing.nombre}]: ") or existing.nombre
        apellido = input(f"Apellido [{existing.apellido}]: ") or existing.apellido
        edad_str = input(f"Edad [{existing.edad}]: ")
        especialidad = input(f"Especialidad [{existing.especialidad}]: ") or existing.especialidad

        try:## un try para por si la edad es string 
            edad = int(edad_str) if edad_str else existing.edad
        except ValueError:
            print("Edad inválida, se mantiene la anterior.")
            edad = existing.edad

        ## se actualiza la nueva informacion
        updated = Maestro(
            id=id_to_edit,
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            especialidad=especialidad
        )

        # ya solo llamamos la funcion de editar para que lo inserte de forma correcta
        if self.maestros.editar(id_to_edit, updated):
            if not self.is_object:
                self.maestros.guardar_en_json(self.path) ## se guarda automatico en el json
            print("Maestro editado correctamente.")
        else:
            print("Error al editar el alumno.")

    def _pedir_datos_maestro(self):
        "solo se solicitan datos" 
        id_maestro = input("ID del maestro: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = input("Edad: ")
        especialidad = input("Especialidad: ")
        return Maestro(id=id_maestro, nombre=nombre, apellido=apellido, edad=edad, especialidad=especialidad)

if __name__ == "__main__":
    # Ejemplo de uso: cargar desde archivo
    ui = MaestroUI(is_object=False)
    maestros = ui.menu_maestros()
    # maestros es la instancia final de Maestro

    # Ejemplo de uso en otro interfaz: usar objeto en memoria
    # ui_obj = MaestroUI(use_object=True)
    # maestros_obj = ui_obj.menu_maestros()
