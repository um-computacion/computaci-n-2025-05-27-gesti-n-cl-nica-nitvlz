#Prueba de la receta

import unittest
from clases.paciente import Paciente
from clases.medico import Medico
from clases.receta import Receta
from clases.excepciones import RecetaInvalidaException

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("12345678", "Lucas Ruiz", "22/05/1995")
        self.medico = Medico("Dra. Ana", "M999")
        self.medicamentos = ["Paracetamol", "Ibuprofeno"]

    def test_crear_receta_valida(self):
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("Lucas Ruiz", str(receta))

    def test_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            Receta(self.paciente, self.medico, [])

    def test_receta_con_multiples_medicamentos(self):
        receta = Receta(self.paciente, self.medico, ["Amoxicilina", "Ibuprofeno", "Paracetamol"])
        receta_str = str(receta)
        self.assertIn("Amoxicilina", receta_str)
        self.assertIn("Ibuprofeno", receta_str)
        self.assertIn("Paracetamol", receta_str)

    def test_nombre_medico_en_receta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol"])
        self.assertIn("Dra. Ana", str(receta))

    def test_formato_fecha_receta(self):
        receta = Receta(self.paciente, self.medico, ["Paracetamol"])
        self.assertRegex(str(receta), r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:")

if __name__ == "__main__":
    unittest.main()