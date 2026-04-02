from models.database import Database


class ClienteModel:
    def __init__(self):
        self.db = Database()

    def insertar(self, nombre, telefono, email, direccion, imagen_path):
        return self.db.execute_procedure('sp_cliente_insertar',
                                         (nombre, telefono, email, direccion, imagen_path))

    def actualizar(self, id, nombre, telefono, email, direccion, imagen_path):
        return self.db.execute_procedure('sp_cliente_actualizar',
                                         (id, nombre, telefono, email, direccion, imagen_path))

    def eliminar(self, id):
        return self.db.execute_procedure('sp_cliente_eliminar', (id,))

    def listar_todos(self):
        return self.db.execute_procedure('sp_cliente_listar') or []

    def buscar(self, busqueda):
        return self.db.execute_procedure('sp_cliente_buscar', (busqueda,)) or []