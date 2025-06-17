#Prueba de las excepciones

import unittest
from clases.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoEncontradoException,
    TurnoDuplicadoException,
    RecetaInvalidaException
)

class TestExcepciones(unittest.TestCase):
    def test_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            raise PacienteNoEncontradoException("Paciente no encontrado")

    def test_medico_no_encontrado(self):
        with self.assertRaises(MedicoNoEncontradoException):
            raise MedicoNoEncontradoException("Médico no encontrado")

    def test_turno_duplicado(self):
        with self.assertRaises(TurnoDuplicadoException):
            raise TurnoDuplicadoException("Turno duplicado")

    def test_receta_invalida(self):
        with self.assertRaises(RecetaInvalidaException):
            raise RecetaInvalidaException("Receta inválida")

if __name__ == "__main__":
    unittest.main()