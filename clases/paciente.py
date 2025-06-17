#Paciente de una clinica

class Paciente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: str):
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
    
    def obtener_dni(self) -> str:
        return self.dni
    
    def __str__(self):
        return f"{self.nombre}, {self.dni}, {self.fecha_nacimiento}"