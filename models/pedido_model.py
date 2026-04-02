from models.database import Database


class PedidoModel:
    def __init__(self):
        self.db = Database()

    def insertar(self, cliente_id, producto_id, cantidad, fecha_pedido, fecha_entrega):
        return self.db.execute_procedure('sp_pedido_insertar',
                                         (cliente_id, producto_id, cantidad, fecha_pedido, fecha_entrega))

    def actualizar(self, id, cliente_id, producto_id, cantidad, fecha_entrega, estado):
        return self.db.execute_procedure('sp_pedido_actualizar',
                                         (id, cliente_id, producto_id, cantidad, fecha_entrega, estado))

    def eliminar(self, id):
        return self.db.execute_procedure('sp_pedido_eliminar', (id,))

    def listar_todos(self):
        return self.db.execute_procedure('sp_pedido_listar') or []

    def listar_por_cliente(self, cliente_id):
        return self.db.execute_procedure('sp_pedido_por_cliente', (cliente_id,)) or []

    def buscar(self, busqueda):
        return self.db.execute_procedure('sp_pedido_buscar', (busqueda,)) or []