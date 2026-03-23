"""
Módulo de conexión a la base de datos SQLite
"""
import sqlite3
import os
import tkinter.messagebox as messagebox

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        # Obtener ruta absoluta de la base de datos
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.db_path = os.path.join(base_dir, 'base_datos', 'textilpro.db')
        self.connection = None
        self.connect()

    def connect(self):
        """Establecer conexión con SQLite"""
        try:
            # Verificar si el archivo existe
            if not os.path.exists(self.db_path):
                messagebox.showerror(
                    "Error de Base de Datos",
                    f"No se encuentra la base de datos:\n{self.db_path}\n\n"
                    f"Ejecuta primero: python crear_bd_final.py"
                )
                return False

            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
            print(f"✅ Conexión exitosa a: {self.db_path}")
            return True

        except Exception as e:
            messagebox.showerror("Error de Base de Datos",
                               f"No se pudo conectar:\n{e}")
            self.connection = None
            return False

    def execute_query(self, query, params=None, fetch_one=False, fetch_all=False):
        """Ejecutar una consulta SQL"""
        if not self.connection:
            if not self.connect():
                return None if not fetch_one and not fetch_all else ([] if fetch_all else None)

        cursor = None
        try:
            cursor = self.connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch_one:
                result = cursor.fetchone()
                return dict(result) if result else None
            elif fetch_all:
                result = cursor.fetchall()
                return [dict(row) for row in result] if result else []
            else:
                self.connection.commit()
                return cursor.lastrowid if cursor.lastrowid else cursor.rowcount

        except Exception as e:
            self.connection.rollback()
            messagebox.showerror("Error en Consulta",
                               f"Error al ejecutar:\n{e}\n\nQuery: {query}")
            return None if not fetch_one and not fetch_all else ([] if fetch_all else None)
        finally:
            if cursor:
                cursor.close()

    def close(self):
        """Cerrar conexión"""
        if self.connection:
            self.connection.close()
            self.connection = None