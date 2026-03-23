"""
DIAGNÓSTICO Y CREACIÓN DE BASE DE DATOS
"""
import sqlite3
import os
import sys

print("=" * 60)
print("DIAGNÓSTICO DE BASE DE DATOS TEXTILPRO")
print("=" * 60)

# 1. Verificar directorio actual
print(f"\n📁 Directorio actual: {os.getcwd()}")

# 2. Crear carpeta base_datos si no existe
if not os.path.exists('base_datos'):
    os.makedirs('base_datos')
    print("✓ Carpeta 'base_datos' creada")

# 3. Ruta completa de la base de datos
db_path = os.path.abspath(os.path.join('base_datos', 'textilpro.db'))
print(f"📄 Ruta de la base de datos: {db_path}")

# 4. Eliminar archivo corrupto si existe
if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print("✓ Archivo anterior eliminado")
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")

# 5. Crear nueva base de datos
print("\n🔧 Creando nueva base de datos...")

try:
    # Conectar (crea el archivo)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    print("✓ Conexión establecida")

    # Crear tabla productos
    cursor.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        categoria TEXT,
        talla TEXT,
        color TEXT,
        precio_compra REAL DEFAULT 0,
        precio_venta REAL DEFAULT 0,
        stock INTEGER DEFAULT 0,
        stock_minimo INTEGER DEFAULT 5,
        imagen_path TEXT,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
        estado INTEGER DEFAULT 1
    )
    ''')
    print("✓ Tabla 'productos' creada")

    # Crear tabla proveedores
    cursor.execute('''
    CREATE TABLE proveedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ruc TEXT NOT NULL UNIQUE,
        nombre TEXT NOT NULL,
        contacto TEXT,
        telefono TEXT,
        email TEXT,
        direccion TEXT,
        imagen_path TEXT,
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
        estado INTEGER DEFAULT 1
    )
    ''')
    print("✓ Tabla 'proveedores' creada")

    # Crear tabla ventas
    cursor.execute('''
    CREATE TABLE ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo_venta TEXT NOT NULL UNIQUE,
        fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
        cliente TEXT,
        total REAL DEFAULT 0,
        estado TEXT DEFAULT 'completada'
    )
    ''')
    print("✓ Tabla 'ventas' creada")

    # Crear tabla detalles_venta
    cursor.execute('''
    CREATE TABLE venta_detalles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        venta_id INTEGER NOT NULL,
        producto_id INTEGER NOT NULL,
        cantidad INTEGER NOT NULL,
        precio_unitario REAL NOT NULL,
        subtotal REAL NOT NULL,
        FOREIGN KEY (venta_id) REFERENCES ventas(id),
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    ''')
    print("✓ Tabla 'venta_detalles' creada")

    # Insertar datos de prueba
    print("\n📦 Insertando datos de prueba...")

    productos = [
        ('PROD001', 'Algodón Premium', 'Algodón 100% orgánico', 'Telas', 'Rollo', 'Blanco', 25, 45, 100),
        ('PROD002', 'Seda Natural', 'Seda pura de alta calidad', 'Telas', 'Rollo', 'Crudo', 80, 150, 50),
        ('PROD003', 'Camisa Casual', 'Camisa de algodón para caballero', 'Prendas', 'M', 'Azul', 15, 35, 80),
        ('PROD004', 'Camisa Formal', 'Camisa de vestir manga larga', 'Prendas', 'L', 'Blanco', 20, 45, 60),
        ('PROD005', 'Pantalón Jean', 'Jean clásico azul', 'Prendas', '32', 'Azul', 25, 55, 40),
    ]

    cursor.executemany('''
        INSERT INTO productos (codigo, nombre, descripcion, categoria, talla, color, precio_compra, precio_venta, stock)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', productos)
    print(f"✓ Insertados {len(productos)} productos")

    proveedores = [
        ('20123456789', 'Textiles del Perú SAC', 'Juan Pérez', '987654321', 'ventas@textilesperu.com',
         'Av. Industrial 123'),
        ('20987654321', 'Insumos Textiles EIRL', 'María López', '987654322', 'maria@insumos.com', 'Calle Comercio 456'),
    ]

    cursor.executemany('''
        INSERT INTO proveedores (ruc, nombre, contacto, telefono, email, direccion)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', proveedores)
    print(f"✓ Insertados {len(proveedores)} proveedores")

    # Confirmar cambios
    conn.commit()
    print("✓ Cambios guardados")

    # Verificar
    print("\n✅ VERIFICANDO BASE DE DATOS")
    cursor.execute("SELECT COUNT(*) FROM productos")
    total = cursor.fetchone()[0]
    print(f"   Total productos: {total}")

    cursor.execute("SELECT COUNT(*) FROM proveedores")
    total = cursor.fetchone()[0]
    print(f"   Total proveedores: {total}")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"\n   Tablas creadas: {len(tables)}")
    for table in tables:
        print(f"   - {table[0]}")

    # Mostrar productos
    print("\n📋 LISTA DE PRODUCTOS:")
    cursor.execute("SELECT id, codigo, nombre, precio_venta, stock FROM productos")
    for row in cursor.fetchall():
        print(f"   {row[0]}. {row[1]} - {row[2]} - ${row[3]} - Stock: {row[4]}")

    # Cerrar conexión
    cursor.close()
    conn.close()

    # Verificar tamaño del archivo
    size = os.path.getsize(db_path)
    print(f"\n💾 Tamaño del archivo: {size} bytes")

    # Verificar que se puede leer
    print("\n🔍 Verificando lectura...")
    test_conn = sqlite3.connect(db_path)
    test_cursor = test_conn.cursor()
    test_cursor.execute("SELECT * FROM productos LIMIT 1")
    test_cursor.fetchone()
    test_conn.close()
    print("✓ La base de datos se puede leer correctamente")

    print("\n" + "=" * 60)
    print("✅ BASE DE DATOS CREADA EXITOSAMENTE")
    print("=" * 60)

except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback

    traceback.print_exc()

input("\nPresiona Enter para salir...")