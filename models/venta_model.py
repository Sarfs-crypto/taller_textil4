"""
Modelo para gestión de ventas
"""
from models.database import Database
from models.producto_model import ProductoModel
from datetime import datetime

class VentaModel:
    def __init__(self):
        self.db = Database()
        self.producto_model = ProductoModel()

    def registrar_venta(self, datos):
        """Registrar una nueva venta con sus detalles"""
        try:
            # Generar código de venta
            codigo_venta = f"VENTA{datetime.now().strftime('%Y%m%d%H%M%S')}"

            # Insertar cabecera de venta
            query_venta = """
                INSERT INTO ventas (codigo_venta, cliente, total)
                VALUES (?, ?, ?)
            """
            venta_id = self.db.execute_query(query_venta, (codigo_venta, datos['cliente'], datos['total']))

            if not venta_id:
                return None

            # Insertar detalles y actualizar stock
            for detalle in datos['detalles']:
                query_detalle = """
                    INSERT INTO venta_detalles (venta_id, producto_id, cantidad, precio_unitario, subtotal)
                    VALUES (?, ?, ?, ?, ?)
                """
                self.db.execute_query(query_detalle, (
                    venta_id, detalle['producto_id'], detalle['cantidad'],
                    detalle['precio_unitario'], detalle['subtotal']
                ))

                # Actualizar stock (restar)
                self.producto_model.actualizar_stock(detalle['producto_id'], -detalle['cantidad'])

            return venta_id

        except Exception as e:
            print(f"Error al registrar venta: {e}")
            return None

    def listar_ventas(self):
        """Listar todas las ventas"""
        query = "SELECT * FROM ventas ORDER BY fecha DESC"
        return self.db.execute_query(query, fetch_all=True)

    def obtener_detalles_venta(self, venta_id):
        """Obtener detalles de una venta"""
        query = """
            SELECT vd.*, p.nombre as producto_nombre, p.codigo as producto_codigo
            FROM venta_detalles vd
            JOIN productos p ON vd.producto_id = p.id
            WHERE vd.venta_id = ?
        """
        return self.db.execute_query(query, (venta_id,), fetch_all=True)

    def obtener_por_id(self, id):
        """Obtener venta por ID"""
        query = "SELECT * FROM ventas WHERE id=?"
        return self.db.execute_query(query, (id,), fetch_one=True)