# clases/especialidad.py

class Especialidad:
    def __init__(self, tipo, dias):
        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]  # normaliza los días

    def obtener_especialidad(self):
        return self.__tipo

    def verificar_dia(self, dia):
        return dia.lower() in self.__dias

    def __str__(self):
        return f"{self.__tipo} (Días: {', '.join(self.__dias)})"
