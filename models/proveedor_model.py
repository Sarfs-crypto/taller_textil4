"""
Modelo para gestión de proveedores
"""
from models.database import Database


class ProveedorModel:
    def __init__(self):
        self.db = Database()

    def insertar(self, datos):
        """Insertar nuevo proveedor"""
        query = """
            INSERT INTO proveedores (ruc, nombre, contacto, telefono, email, direccion, imagen_path)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            datos['ruc'], datos['nombre'], datos['contacto'],
            datos['telefono'], datos['email'], datos['direccion'], datos.get('imagen_path')
        )
        return self.db.execute_query(query, params)

    def actualizar(self, id, datos):
        """Actualizar proveedor existente"""
        query = """
            UPDATE proveedores SET ruc=?, nombre=?, contacto=?, telefono=?, email=?, direccion=?, imagen_path=?
            WHERE id=?
        """
        params = (
            datos['ruc'], datos['nombre'], datos['contacto'],
            datos['telefono'], datos['email'], datos['direccion'], datos.get('imagen_path'), id
        )
        return self.db.execute_query(query, params)

    def eliminar(self, id):
        """Eliminar proveedor (soft delete)"""
        query = "UPDATE proveedores SET estado=0 WHERE id=?"
        return self.db.execute_query(query, (id,))

    def listar_todos(self):
        """Listar todos los proveedores activos"""
        query = "SELECT * FROM proveedores WHERE estado=1 ORDER BY nombre"
        return self.db.execute_query(query, fetch_all=True)

    def buscar(self, busqueda):
        """Buscar proveedores por RUC o nombre"""
        query = """
            SELECT * FROM proveedores 
            WHERE estado=1 AND (ruc LIKE ? OR nombre LIKE ?)
            ORDER BY nombre
        """
        like = f"%{busqueda}%"
        return self.db.execute_query(query, (like, like), fetch_all=True)

    def obtener_por_id(self, id):
        """Obtener proveedor por ID"""
        query = "SELECT * FROM proveedores WHERE id=?"
        return self.db.execute_query(query, (id,), fetch_one=True)