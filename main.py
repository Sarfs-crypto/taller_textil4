"""
TextilPro - Sistema de Gestión para Industria Textil
Autor: Basado en taller_PO-industria-textil
"""

import tkinter as tk
from controllers.main_controller import MainController

class TextilProApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TextilPro - Sistema de Gestión Textil")
        self.root.geometry("1400x800")

        # Configurar favicon
        try:
            self.root.iconbitmap("assets/favicon.ico")
        except:
            pass

        # Iniciar controlador principal
        self.controller = MainController(self.root)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TextilProApp()
    app.run()