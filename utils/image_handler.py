from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import os


class ImageHandler:
    def __init__(self):
        self.formatos_permitidos = ['.jpg', '.jpeg', '.png', '.gif']
        self.tamano_maximo = 5 * 1024 * 1024
        self.carpeta_imagenes = "assets/images"
        os.makedirs(self.carpeta_imagenes, exist_ok=True)

    def seleccionar_imagen(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Imágenes", "*.jpg *.jpeg *.png *.gif")]
        )
        if filename:
            ext = os.path.splitext(filename)[1].lower()
            if ext not in self.formatos_permitidos:
                messagebox.showerror("Error", f"Formato no permitido. Use: {', '.join(self.formatos_permitidos)}")
                return None
            if os.path.getsize(filename) > self.tamano_maximo:
                messagebox.showerror("Error", "La imagen excede 5MB")
                return None
            return filename
        return None

    def procesar_imagen(self, origen_path, nombre_archivo=None, tamaño=(200, 200)):
        try:
            img = Image.open(origen_path)
            if img.mode in ('RGBA', 'LA', 'P'):
                bg = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                bg.paste(img, mask=img.split()[-1])
                img = bg
            img.thumbnail(tamaño, Image.Resampling.LANCZOS)
            nueva = Image.new('RGB', tamaño, (255, 255, 255))
            x = (tamaño[0] - img.size[0]) // 2
            y = (tamaño[1] - img.size[1]) // 2
            nueva.paste(img, (x, y))
            if not nombre_archivo:
                nombre_archivo = f"img_{hash(origen_path)}.jpg"
            destino = os.path.join(self.carpeta_imagenes, f"{nombre_archivo}.jpg")
            nueva.save(destino, 'JPEG', quality=85)
            return destino
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo procesar imagen:\n{e}")
            return None

    def cargar_para_tk(self, imagen_path, tamaño=(150, 150)):
        try:
            if not os.path.exists(imagen_path):
                return None
            img = Image.open(imagen_path)
            img.thumbnail(tamaño, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except:
            return None