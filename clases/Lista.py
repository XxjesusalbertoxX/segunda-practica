# Lista.py
import json, os

class Lista:
    def __init__(self):
        self.lista = []
        self.es_lista = True

    @classmethod
    def cargar_desde_json(cls, filename):
        # ubicación del archivo
        path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        contenedor = cls()  # instancia vacía de la subclase
        if isinstance(data, list):
            for item in data:
                # aquí sí llamamos al from_dict apropiado de la subclase
                contenedor.agregar(cls.from_dict(item))
        else:
            # JSON puede ser un solo dict
            contenedor.agregar(cls.from_dict(data))
        return contenedor

    def convertir_a_diccionario(self):
        if self.es_lista and isinstance(self.lista, list):
            return [ item.convertir_a_diccionario() for item in self.lista ]
        # else: convierte un solo objeto
        result = {}
        for k, v in vars(self).items():
            if k in ('lista', 'es_lista'): continue
            if hasattr(v, 'convertir_a_diccionario'):
                result[k] = v.convertir_a_diccionario()
            else:
                result[k] = v
        return result

    def guardar_en_json(self, filename):
        json_data = self.convertir_a_diccionario()
        path = filename if os.path.isabs(filename) else os.path.join(os.path.dirname(__file__), filename)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

    def agregar(self, data):
        if self.es_lista:
            self.lista.append(data)
            return True
        return False

    def eliminar(self, id=None):
        if self.es_lista:
            if id is None:
                self.lista = []
                return True
            for i, item in enumerate(self.lista):
                if getattr(item, 'id', None) == id:
                    del self.lista[i]
                    return True
        return False

    def editar(self, sended_id, data):
        if self.es_lista:
            for idx, item in enumerate(self.lista):
                if getattr(item, 'id', None) == sended_id:
                    self.lista[idx] = data
                    return True
        return False

    def mostrar(self):
        print(json.dumps(self.convertir_a_diccionario(), ensure_ascii=False, indent=2))
