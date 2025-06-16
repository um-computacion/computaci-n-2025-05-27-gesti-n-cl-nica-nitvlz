#Excepciones personalizadas

class PacienteNoEncontradoException(Exception):
    pass

class MedicoNoEncontradoException(Exception):
    def __str__(self):
        return "Médico no encontrado."

class TurnoDuplicadoException(Exception):
    pass

class TurnoOcupadoException(Exception):
    pass

class RecetaInvalidaException(Exception):
    pass




