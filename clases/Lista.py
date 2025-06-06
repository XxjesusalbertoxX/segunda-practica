import json
import os

class Lista:
    def __init__(self):
        self.lista = []
        self.es_lista = True
        

    @classmethod
    def cargar_desde_json(cls, filename):
        if not os.path.isabs(filename):
            path = os.path.join(os.path.dirname(__file__), filename)
        else:
            path = filename
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        objetos = cls.from_dict(data) 
        return objetos

    @classmethod
    def from_dict(cls, data):
        objetos = cls()
        if isinstance(data, list):
            for item in data:
                # Siempre llama a from_dict de la subclase, excepto si es la base
                if cls == Lista:
                    objetos.agregar(item)
                else:
                    objetos.agregar(cls.from_dict(item))
        else:
            if cls == Lista:
                objetos.agregar(data)#si es una lista, agrega el objeto directamente
            else:
                objetos.agregar(cls.from_dict(data))#si no es una lista convierto cada objeto de forma recursiva para agregarlo
        return objetos
    
    def convertir_a_diccionario(self):
        if hasattr(self, "lista") and isinstance(self.lista, list) and self.lista:
            # Si es una lista, convierte cada elemento a diccionario
            return [
                item.convertir_a_diccionario() for item in self.lista
            ]
        else:
            result = {}
            for k, v in vars(self).items():
                if k in ("lista", "es_lista"): 
                    continue
                if isinstance(v, list):
                    result[k] = [
                        item.convertir_a_diccionario() for item in v
                    ]
                elif hasattr(v, "convertir_a_diccionario"):
                    # Si el valor es un objeto personalizado, lo convierte recursivamente
                    result[k] = v.convertir_a_diccionario()
                else:
                    result[k] = v
            return result

    def guardar_en_json(self, filename):
        json_data = self.convertir_a_diccionario()
        if not os.path.isabs(filename): # eso verifica si la ruta es absoluta o no true/false
            path = os.path.join(os.path.dirname(__file__), filename) # si no es absoluta, la convierte en una ruta absoluta
        else:
            path = filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)#el .dump da el formato de json 

    def mostrar_uno(self, id):
        if self.es_lista:
            for item in self.lista:
                if item.id == id:
                    print(item)
        return False

    def agregar(self, data):
        if self.es_lista:
            self.lista.append(data)
        else:
            return False
    
    def mostrar(self):
        print(json.dumps(self.convertir_a_diccionario(), ensure_ascii=False, indent=2))

    def eliminar(self, id):
        if self.es_lista:
            for i, item in enumerate(self.lista):
                if item.id == id:
                    del self.lista[i]
                    return True
        return False

    def editar(self, sended_id, data):
        if self.es_lista:
            for item in self.lista:
                if item.id == sended_id:
                    item = data
        return False