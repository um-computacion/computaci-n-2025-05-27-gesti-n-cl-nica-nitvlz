#Receta de un medico de una clinica

from datetime import datetime
from clases.excepciones import RecetaInvalidaException

class Receta:
    def __init__(self, paciente, medico, medicamentos: list[str]):
        if not medicamentos:
            raise RecetaInvalidaException("La receta debe contener al menos un medicamento.")
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        return f"Receta(\n  Paciente({self.__paciente}),\n  Medico({self.__medico}),\n  [{medicamentos_str}],\n  {self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}\n)"