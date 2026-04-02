from models.database import Database


class ProductoModel:
    def __init__(self):
        self.db = Database()

    def insertar(self, nombre, descripcion, precio, stock, imagen_path):
        return self.db.execute_procedure('sp_producto_insertar',
                                         (nombre, descripcion, precio, stock, imagen_path))

    def actualizar(self, id, nombre, descripcion, precio, stock, imagen_path):
        return self.db.execute_procedure('sp_producto_actualizar',
                                         (id, nombre, descripcion, precio, stock, imagen_path))

    def eliminar(self, id):
        return self.db.execute_procedure('sp_producto_eliminar', (id,))

    def listar_todos(self):
        return self.db.execute_procedure('sp_producto_listar') or []

    def buscar(self, busqueda):
        return self.db.execute_procedure('sp_producto_buscar', (busqueda,)) or []