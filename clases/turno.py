
#Turno de una clinica

from datetime import datetime

class Turno:
    def __init__(self, paciente, medico, fecha_hora: datetime, especialidad: str):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad
    
    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __str__(self) -> str:
        return f"Turno(\n  Paciente({self.__paciente}),\n  Medico({self.__medico}),\n  {self.__fecha_hora},\n  {self.__especialidad}\n)"
