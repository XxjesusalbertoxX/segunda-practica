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
            return vars(self)







    def mostrar(self):
        if self.lista:
            print("Numero de Items:" + str(len(self.lista)))
            #for item in self.lista:
            #    item.mostrar()
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

    def exportar(self, ruta):
        with open(ruta, 'w') as file:
            import json
            json.dump(self.convertir_a_diccionario(), file, indent=4)
        return True


    def convertir_json_objeto(self, data):
        if self.es_lista:
            self.lista = []
            for item in data:
                if 'lista' in item:
                    del item['lista']
                if 'es_lista' in item:
                    del item['es_lista']
                self.lista.append(self.__class__(**item))
        else:
            for key, value in data.items():
                setattr(self, key, value)
        return True


    def importar(self, ruta):
        with open(ruta, 'r') as file:
            import json
            data = json.load(file)

            return self.convertir_json_objeto(data)
