"""
Modelo para gestión de productos
"""
from models.database import Database


class ProductoModel:
    def __init__(self):
        self.db = Database()

    def insertar(self, datos):
        """Insertar nuevo producto"""
        query = """
            INSERT INTO productos (codigo, nombre, descripcion, categoria, talla, color, 
                                   precio_compra, precio_venta, stock, stock_minimo, imagen_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            datos['codigo'], datos['nombre'], datos['descripcion'], datos['categoria'],
            datos['talla'], datos['color'], datos['precio_compra'], datos['precio_venta'],
            datos['stock'], datos['stock_minimo'], datos.get('imagen_path')
        )
        return self.db.execute_query(query, params)

    def actualizar(self, id, datos):
        """Actualizar producto existente"""
        query = """
            UPDATE productos SET codigo=?, nombre=?, descripcion=?, categoria=?, talla=?, 
                   color=?, precio_compra=?, precio_venta=?, stock=?, stock_minimo=?, imagen_path=?
            WHERE id=?
        """
        params = (
            datos['codigo'], datos['nombre'], datos['descripcion'], datos['categoria'],
            datos['talla'], datos['color'], datos['precio_compra'], datos['precio_venta'],
            datos['stock'], datos['stock_minimo'], datos.get('imagen_path'), id
        )
        return self.db.execute_query(query, params)

    def eliminar(self, id):
        """Eliminar producto (soft delete)"""
        query = "UPDATE productos SET estado=0 WHERE id=?"
        return self.db.execute_query(query, (id,))

    def listar_todos(self):
        """Listar todos los productos activos"""
        query = "SELECT * FROM productos WHERE estado=1 ORDER BY nombre"
        return self.db.execute_query(query, fetch_all=True)

    def buscar(self, busqueda):
        """Buscar productos por código o nombre"""
        query = """
            SELECT * FROM productos 
            WHERE estado=1 AND (codigo LIKE ? OR nombre LIKE ?)
            ORDER BY nombre
        """
        like = f"%{busqueda}%"
        return self.db.execute_query(query, (like, like), fetch_all=True)

    def obtener_por_id(self, id):
        """Obtener producto por ID"""
        query = "SELECT * FROM productos WHERE id=?"
        return self.db.execute_query(query, (id,), fetch_one=True)

    def actualizar_stock(self, id, cantidad):
        """Actualizar stock (positivo o negativo)"""
        query = "UPDATE productos SET stock = stock + ? WHERE id=?"
        return self.db.execute_query(query, (cantidad, id))