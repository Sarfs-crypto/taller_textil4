# TextilPro - Sistema de Gestión para Industria Textil

Sistema de escritorio desarrollado en Python para la gestión de productos, proveedores y ventas en la industria textil.

## Características

- **Módulo de Productos**: CRUD completo con validaciones, gestión de imágenes y stock
- **Módulo de Proveedores**: Gestión de proveedores con validación de RUC y email
- **Módulo de Ventas**: Registro de ventas con carrito de compras y actualización automática de stock
- **Validaciones**: Campos numéricos, emails, RUC, teléfonos con mensajes de error
- **Exportación**: Exportar datos a Excel y PDF con formato profesional
- **Imágenes**: Gestión de imágenes con PILLOW (redimensionamiento, preview)
- **Temas**: Interfaz con temas claro/oscuro intercambiables

## Tecnologías

- Python 3.8+
- Tkinter (GUI)
- SQLite (Base de datos)
- Pillow (Imágenes)
- openpyxl (Excel)
- reportlab (PDF)

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/Sarfs-crypto/taller_PO-industria-textil.git

# Instalar dependencias
pip install Pillow openpyxl reportlab

# Ejecutar
python main.py