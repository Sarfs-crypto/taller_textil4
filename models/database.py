import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as messagebox


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='textil_db',
                user='root',
                password='',
                port='3306'
            )
            if self.connection.is_connected():
                print("✓ Conectado a MySQL")
        except Error as e:
            messagebox.showerror("Error", f"No se pudo conectar:\n{e}")
            self.connection = None

    def execute_procedure(self, procedure_name, params=None):
        if not self.connection:
            self.connect()
        cursor = None
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.callproc(procedure_name, params)
            else:
                cursor.callproc(procedure_name)
            result = []
            for res in cursor.stored_results():
                result = res.fetchall()
                break
            self.connection.commit()
            return result
        except Error as e:
            self.connection.rollback()
            messagebox.showerror("Error", f"Error en {procedure_name}:\n{e}")
            return None
        finally:
            if cursor:
                cursor.close()