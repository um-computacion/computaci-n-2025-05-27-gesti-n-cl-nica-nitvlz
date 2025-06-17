#Historia clinica de un paciente en una clinica

class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta):
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos)

    def obtener_recetas(self):
        return list(self.__recetas)

    def __str__(self):
        resultado = [f"HistoriaClinica(\n  Paciente({self.__paciente}),"]
        resultado.append("  Turnos:[")
        resultado.extend([f"    {turno}" for turno in self.__turnos])
        resultado.append("  ],\n  Recetas:[")
        resultado.extend([f"    {receta}" for receta in self.__recetas])
        resultado.append("  ]\n)")
        return "\n".join(resultado)