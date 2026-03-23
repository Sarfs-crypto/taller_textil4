"""
Prueba mínima de conexión a base de datos
"""
import sqlite3
import os

print("=" * 50)
print("PRUEBA MÍNIMA DE CONEXIÓN")
print("=" * 50)

db_path = os.path.join('base_datos', 'textilpro.db')
print(f"Buscando BD en: {db_path}")

if not os.path.exists(db_path):
    print("❌ La base de datos NO existe")
    print("Ejecuta primero: python diagnostico_bd.py")
else:
    print("✅ La base de datos existe")

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()
        print(f"\nTablas encontradas: {len(tables)}")

        cursor.execute("SELECT * FROM productos LIMIT 3")
        productos = cursor.fetchall()
        print(f"\nProductos encontrados: {len(productos)}")

        for p in productos:
            print(f"  - {p[1]}: {p[2]} (${p[8]})")

        conn.close()
        print("\n✅ Prueba exitosa!")

    except Exception as e:
        print(f"❌ Error: {e}")

input("\nPresiona Enter para salir...")