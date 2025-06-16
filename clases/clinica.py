#Base de datos de una Clinica

from datetime import datetime
from clases.paciente import Paciente
from clases.medico import Medico
from clases.turno import Turno
from clases.receta import Receta
from clases.historiaclinica import HistoriaClinica
from clases.excepciones import PacienteNoEncontradoException
from clases.excepciones import TurnoOcupadoException
from clases.excepciones import MedicoNoEncontradoException

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    def obtener_medico_por_matricula(self, matricula: str) -> Medico | None:
        return self.__medicos.get(matricula)


    def agregar_paciente(self, paciente: Paciente):
        self.__pacientes[paciente.obtener_dni()] = paciente
        self.__historias_clinicas[paciente.obtener_dni()] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        self.__medicos[medico.obtener_matricula()] = medico

    def agendar_turno(self, dni, matricula, fecha_hora):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException()
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException()
        for t in self.__turnos:
            if t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException()
        if fecha_hora < datetime.now(): 
            raise ValueError("No se pueden agendar turnos en el pasado")

        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]

        dias_traducidos = {
        'Monday': 'lunes',
        'Tuesday': 'martes',
        'Wednesday': 'miércoles',
        'Thursday': 'jueves',
        'Friday': 'viernes',
        'Saturday': 'sábado',
        'Sunday': 'domingo'
        }
        dia = dias_traducidos[fecha_hora.strftime("%A")]
        
        especialidad = medico.obtener_especialidad_para_dia(dia)
        if not especialidad:
            raise ValueError("El médico no atiende ese día")

        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException()
        if matricula not in self.__medicos:
            raise MedicoNoEncontradoException()
        receta = Receta(self.__pacientes[dni], self.__medicos[matricula], medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    def obtener_historia_clinica(self, dni):
        if dni not in self.__historias_clinicas:
            raise PacienteNoEncontradoException()
        return self.__historias_clinicas[dni]

    @property
    def pacientes(self):
        return self.__pacientes

    @property
    def medicos(self):
        return self.__medicos

    @property
    def turnos(self):
        return self.__turnos