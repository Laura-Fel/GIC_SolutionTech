import json
import os

class clientes_servicios:
    def __init__(self, archivo='base_datos/clientes.json'):
        self.archivo = archivo
        self.clientes = self.cargar_datos()

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []

    def guardar_datos(self):
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.clientes, f, indent=4, ensure_ascii=False)

    def registrar(self, objeto_cliente):
        self.clientes.append(objeto_cliente.to_dict())
        self.guardar_datos()