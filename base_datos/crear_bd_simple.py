"""
Script simple para crear la base de datos SQLite de TextilPro
"""
import sqlite3
import os

print("="*50)
print("CREANDO BASE DE DATOS TEXTILPRO")
print("="*50)

# Asegurar que la carpeta existe
if not os.path.exists('base_datos'):
    os.makedirs('base_datos')
    print("✓ Carpeta base_datos creada")

# Ruta completa
db_path = os.path.join('base_datos', 'textilpro.db')
print(f"\nCreando base de datos en: {db_path}")

# Eliminar si existe
if os.path.exists(db_path):
    os.remove(db_path)
    print("✓ Archivo anterior eliminado")

# Conectar (crea el archivo)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("\nCreando tablas...")

# Tabla de productos
cursor.execute('''
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL UNIQUE,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    categoria TEXT,
    talla TEXT,
    color TEXT,
    precio_compra REAL NOT NULL,
    precio_venta REAL NOT NULL,
    stock INTEGER DEFAULT 0,
    stock_minimo INTEGER DEFAULT 5,
    imagen_path TEXT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    estado INTEGER DEFAULT 1
)
''')
print("✓ Tabla 'productos' creada")

# Tabla de proveedores
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

# Tabla de ventas
cursor.execute('''
CREATE TABLE ventas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo_venta TEXT NOT NULL UNIQUE,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    cliente TEXT,
    total REAL NOT NULL,
    estado TEXT DEFAULT 'completada'
)
''')
print("✓ Tabla 'ventas' creada")

# Tabla de detalles de venta
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

print("\nInsertando datos de ejemplo...")

# Productos de ejemplo
productos = [
    ('TEL001', 'Algodón Premium', 'Algodón 100% orgánico', 'Telas', 'Rollo', 'Blanco', 25.00, 45.00, 100),
    ('TEL002', 'Seda Natural', 'Seda pura de alta calidad', 'Telas', 'Rollo', 'Crudo', 80.00, 150.00, 50),
    ('CAM001', 'Camisa Casual', 'Camisa de algodón para caballero', 'Prendas', 'M', 'Azul', 15.00, 35.00, 80),
    ('CAM002', 'Camisa Formal', 'Camisa de vestir manga larga', 'Prendas', 'L', 'Blanco', 20.00, 45.00, 60),
    ('PAN001', 'Pantalón Jean', 'Jean clásico azul', 'Prendas', '32', 'Azul', 25.00, 55.00, 40),
    ('HIL001', 'Hilo Poliéster', 'Hilo de alta resistencia', 'Insumos', '500m', 'Negro', 5.00, 12.00, 200),
]

cursor.executemany('''
    INSERT INTO productos (codigo, nombre, descripcion, categoria, talla, color, precio_compra, precio_venta, stock)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', productos)
print(f"✓ Insertados {len(productos)} productos")

# Proveedores de ejemplo
proveedores = [
    ('20123456789', 'Textiles del Perú SAC', 'Juan Pérez', '987654321', 'ventas@textilesperu.com', 'Av. Industrial 123, Lima'),
    ('20987654321', 'Insumos Textiles EIRL', 'María López', '987654322', 'maria@insumostextiles.com', 'Calle Comercio 456, Arequipa'),
    ('20456789012', 'Moda Express SAC', 'Carlos Ruiz', '987654323', 'carlos@modaexpress.com', 'Jr. La Moda 789, Trujillo'),
]

cursor.executemany('''
    INSERT INTO proveedores (ruc, nombre, contacto, telefono, email, direccion)
    VALUES (?, ?, ?, ?, ?, ?)
''', proveedores)
print(f"✓ Insertados {len(proveedores)} proveedores")

# Ventas de ejemplo
cursor.execute('''
    INSERT INTO ventas (codigo_venta, cliente, total)
    VALUES ('VENTA001', 'Cliente Mayorista', 1250.00)
''')
cursor.execute('''
    INSERT INTO ventas (codigo_venta, cliente, total)
    VALUES ('VENTA002', 'Tienda de Ropa La Elegante', 850.00)
''')
print("✓ Insertadas 2 ventas")

# Confirmar cambios
conn.commit()

print("\n" + "="*50)
print("VERIFICANDO BASE DE DATOS")
print("="*50)

# Verificar
cursor.execute("SELECT COUNT(*) FROM productos")
productos_count = cursor.fetchone()[0]
print(f"✓ Productos: {productos_count}")

cursor.execute("SELECT COUNT(*) FROM proveedores")
proveedores_count = cursor.fetchone()[0]
print(f"✓ Proveedores: {proveedores_count}")

cursor.execute("SELECT COUNT(*) FROM ventas")
ventas_count = cursor.fetchone()[0]
print(f"✓ Ventas: {ventas_count}")

# Mostrar productos
print("\n📦 Lista de productos:")
cursor.execute("SELECT id, codigo, nombre, precio_venta, stock FROM productos LIMIT 5")
for row in cursor.fetchall():
    print(f"   {row[0]}. {row[1]} - {row[2]} - ${row[3]} - Stock: {row[4]}")

# Cerrar conexión
cursor.close()
conn.close()

print(f"\n✅ Base de datos creada exitosamente en: {db_path}")
print(f"   Tamaño del archivo: {os.path.getsize(db_path)} bytes")

# Verificar que el archivo existe y es válido
try:
    test_conn = sqlite3.connect(db_path)
    test_cursor = test_conn.cursor()
    test_cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = test_cursor.fetchall()
    print(f"\n✅ Tablas en la base de datos: {len(tables)}")
    for table in tables:
        print(f"   - {table[0]}")
    test_conn.close()
except Exception as e:
    print(f"\n❌ Error al verificar: {e}")

print("\n" + "="*50)
input("Presiona Enter para salir...")