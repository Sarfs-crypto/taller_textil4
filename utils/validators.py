import re
from datetime import datetime


class Validators:

    @staticmethod
    def solo_numeros(texto):
        if texto == "":
            return True
        try:
            float(texto)
            return True
        except:
            return False

    @staticmethod
    def validar_email(email):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, email) is not None

    @staticmethod
    def validar_longitud(texto, min_len=3, max_len=200):
        if not texto:
            return False
        return min_len <= len(texto) <= max_len

    @staticmethod
    def validar_precio(precio):
        try:
            return float(precio) > 0
        except:
            return False

    @staticmethod
    def validar_fecha(fecha_str):
        try:
            if fecha_str:
                datetime.strptime(fecha_str, '%Y-%m-%d')
            return True
        except:
            return False