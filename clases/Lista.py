class Lista:
    def __init__(self):
        self.lista = []
        self.es_lista = True

    #convertir a dicionario el objeto o los atributos de la lista
    def convertir_a_diccionario(self):
        if self.lista:
            return [vars(item) for item in self.lista]
        else:
            return vars(self)

    def mostrar(self):
        if self.lista:
            print("Numero de Items:" + str(len(self.lista)))
            #for item in self.lista:
            #    item.mostrar()
        else:
            for atributo, valor in vars(self).items():
                if not atributo.startswith("__") and atributo != "es_lista" and atributo != "lista":
                    if hasattr(valor, "__str__"):
                        print(f"{atributo}: {valor}")
                    else:
                        print(f"{atributo}: {valor}")

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