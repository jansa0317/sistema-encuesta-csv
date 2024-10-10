import pytest
from models.encuesta import Encuesta, Pregunta
from models.usuario import Usuario
from models.respuesta import Respuesta  # Asegúrate de importar Respuesta
from models.grupo import Grupo

# Pruebas para la clase Encuesta
def test_crear_encuesta():
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    assert encuesta.titulo == "Encuesta de Satisfacción"

def test_agregar_pregunta():
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    pregunta1 = Pregunta(texto="¿Cómo calificaría el servicio?")
    pregunta2 = Pregunta(texto="¿Recomendaría el servicio?")
    pregunta3 = Pregunta(texto="¿Cómo mejoraría el servicio?")
    encuesta.agregar_pregunta(pregunta1)
    encuesta.agregar_pregunta(pregunta2)
    encuesta.agregar_pregunta(pregunta3)
    assert len(encuesta.preguntas) == 3

# Pruebas para la clase Pregunta
def test_crear_pregunta():
    pregunta = Pregunta(texto="¿Cuál es su edad?")
    assert pregunta.texto == "¿Cuál es su edad?"

# Pruebas para la clase Respuesta
def test_crear_respuesta():
    usuario = Usuario(id=1, nombre="Juan Pérez", email="juan@example.com", edad=30, sexo='M')
    pregunta = Pregunta(texto="¿Cómo calificaría el servicio?")
    respuesta = Respuesta(pregunta, usuario, "Excelente")
    assert respuesta.valor == "Excelente"

# Pruebas para la clase Usuario
def test_crear_usuario():
    usuario = Usuario(id=2, nombre="Ana García", email="ana@example.com", edad=25, sexo='F')
    assert usuario.nombre == "Ana García"

# Pruebas para la clase Grupo
def test_crear_grupo():
    grupo = Grupo(nombre="Clientes VIP", criterios={"edad": ">= 30"})
    assert grupo.nombre == "Clientes VIP"

# Pruebas para la integración entre clases
def test_encuesta_con_grupo():
    grupo = Grupo(nombre="Clientes VIP")
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03")
    encuesta.aplicar_a_grupo(grupo)
    assert encuesta.grupo == grupo
