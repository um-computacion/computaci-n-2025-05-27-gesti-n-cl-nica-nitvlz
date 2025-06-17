
# 🏥 Sistema de Gestión de una Clínica

Alumno: Martín Velázquez
Legajo: 63271
Carrera: Ingeniería Informática
Fecha: Junio 2025

Este proyecto implementa un sistema completo para gestionar una clínica médica utilizando Python. Permite registrar pacientes y médicos, agendar turnos, emitir recetas y consultar historias clínicas, todo desde una interfaz de línea de comandos (CLI).

## 📁 Estructura del Proyecto

```bash
CLINICA COMPU/
├── clases/
│   ├── __init__.py
│   ├── clinica.py              # Lógica principal de la clínica
│   ├── especialidad.py         # Modelo de especialidades médicas
│   ├── excepciones.py          # Excepciones personalizadas
│   ├── historialclinica.py     # Manejo de la historia clínica
│   ├── medico.py               # Clase Médico
│   ├── paciente.py             # Clase Paciente
│   ├── receta.py               # Emisión de recetas médicas
│   └── turno.py                # Agendamiento y control de turnos
│
├── tests/                      # Pruebas unitarias
│   ├── __init__.py
│   ├── test_clinica.py
│   ├── test_especialidad.py
│   ├── test_excepciones.py
│   ├── test_historiaclinica.py
│   ├── test_medico.pypython3 -m unittest

│   └── test_turno.py
│
├── cli.py                      # Consola de usuario (CLI)
├── README_yo.md                # Documento personal del autor
```

## ▶️ Ejecución del Sistema

Para ejecutar el sistema, asegurate de tener Python instalado (3.7 o superior). Luego corré el archivo `cli.py`:

```bash
python cli.py
```

Se mostrará un menú interactivo en consola donde podés:

# 🏥 Sistema de Gestión de una Clínica

Este proyecto implementa un sistema completo para gestionar una clínica médica utilizando Python. Permite registrar pacientes y médicos, agendar turnos, emitir recetas y consultar historias clínicas, todo desde una interfaz de línea de comandos (CLI).

## 📁 Estructura del Proyecto

```bash
CLINICA COMPU/
├── clases/
│   ├── __init__.py
│   ├── clinica.py              # Lógica principal de la clínica
│   ├── especialidad.py         # Modelo de especialidades médicas
│   ├── excepciones.py          # Excepciones personalizadas
│   ├── historialclinica.py     # Manejo de la historia clínica
│   ├── medico.py               # Clase Médico
│   ├── paciente.py             # Clase Paciente
│   ├── receta.py               # Emisión de recetas médicas
│   └── turno.py                # Agendamiento y control de turnos
│
├── tests/                      # Pruebas unitarias
│   ├── __init__.py
│   ├── test_clinica.py
│   ├── test_especialidad.py
│   ├── test_excepciones.py
│   ├── test_historiaclinica.py
│   ├── test_medico.pypython3 -m unittest

│   └── test_turno.py
│
├── cli.py                      # Consola de usuario (CLI)
├── README_yo.md                # Documento personal del autor
```

## ▶️ Ejecución del Sistema

Para ejecutar el sistema, asegurate de tener Python instalado (3.7 o superior). Luego corré el archivo `cli.py`:

```bash
python cli.py
```

Se mostrará un menú interactivo en consola donde podés:

1. Agregar paciente  
2. Agregar médico  
3. Agendar turno  
4. Emitir receta  
5. Ver historia clínica  
6. Ver todos los turnos  
7. Ver todos los pacientes  
8. Ver todos los médicos  
9. Salir

## 🧠 Diseño General

El diseño sigue una arquitectura orientada a objetos modular:

- **`Clinica`** es la clase central, que coordina pacientes, médicos, turnos y recetas.
- **`Paciente`** y **`Medico`** son modelos que contienen información básica.
- **`Especialidad`** permite asignar distintos días de atención por tipo.
- **`Turno`** y **`Receta`** encapsulan la lógica de agendamiento y prescripción.
- **`HistorialClinica`** registra todas las recetas emitidas a un paciente.
- **`CLI`** (interfaz de línea de comandos) facilita la interacción con el sistema.

Se aplican buenas prácticas como encapsulamiento, manejo de excepciones personalizadas (`PacienteNoEncontradoException`, `TurnoOcupadoException`, etc.) y separación clara entre lógica y presentación.

## 🧪 Cobertura de Pruebas

El sistema cuenta con pruebas unitarias organizadas en la carpeta `/tests`, una por cada clase clave del sistema:

- Validación de lógica de negocio.
- Verificación de excepciones personalizadas.
- Integración básica entre componentes.

Podés correr los tests con:

```bash
python -m unittest discover tests
```

## 👤 Autor

Desarrollado por **Martín Velázquez** como parte de un proyecto académico.

1. Agregar paciente  
2. Agregar médico  
3. Agendar turno  
4. Emitir receta  
5. Ver historia clínica  
6. Ver todos los turnos  
7. Ver todos los pacientes  
8. Ver todos los médicos  
9. Salir

## 🧠 Diseño General

El diseño sigue una arquitectura orientada a objetos modular:

- **`Clinica`** es la clase central, que coordina pacientes, médicos, turnos y recetas.
- **`Paciente`** y **`Medico`** son modelos que contienen información básica.
- **`Especialidad`** permite asignar distintos días de atención por tipo.
- **`Turno`** y **`Receta`** encapsulan la lógica de agendamiento y prescripción.
- **`HistorialClinica`** registra todas las recetas emitidas a un paciente.
- **`CLI`** (interfaz de línea de comandos) facilita la interacción con el sistema.
1. Agregar paciente  

Se aplican buenas prácticas como encapsulamiento, manejo de excepciones personalizadas (`PacienteNoEncontradoException`, `TurnoOcupadoException`, etc.) y separación clara entre lógica y presentación.

## 🧪 Cobertura de Pruebas

El sistema cuenta con pruebas unitarias organizadas en la carpeta `/tests`, una por cada clase clave del sistema:

- Validación de lógica de negocio.
- Verificación de excepciones personalizadas.
- Integración básica entre componentes.

Podés correr los tests con:

```bash
python -m unittest discover tests
```
