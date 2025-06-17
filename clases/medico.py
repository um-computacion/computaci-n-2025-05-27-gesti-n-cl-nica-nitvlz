#Medico de una clinica

from clases.especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list[Especialidad] = None):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades or []

    def agregar_especialidad(self, especialidad: Especialidad):
        if all(e.obtener_especialidad() != especialidad.obtener_especialidad() for e in self.__especialidades):
            self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for esp in self.__especialidades:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = ",\n ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre}, {self.__matricula}, [\n {especialidades_str}\n]"