# corregir.py
import os

carpetas = ['controllers', 'views', 'models', 'utils']

for carpeta in carpetas:
    if os.path.exists(carpeta):
        for archivo in os.listdir(carpeta):
            if archivo.endswith('.py'):
                ruta = os.path.join(carpeta, archivo)
                with open(ruta, 'r', encoding='utf-8') as f:
                    contenido = f.read()

                # Eliminar el + al inicio si existe
                if contenido.startswith('+'):
                    contenido = contenido[1:]
                    with open(ruta, 'w', encoding='utf-8') as f:
                        f.write(contenido)
                    print(f"✓ Corregido: {ruta}")

print("Archivos corregidos")