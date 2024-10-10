# models/encuesta.py

class Pregunta:
    def __init__(self, texto):
        self.texto = texto

class Grupo:
    def __init__(self, nombre, criterios=None):
        self.nombre = nombre
        self.criterios = criterios if criterios else {}

class Encuesta:
    def __init__(self, titulo, fechaCreacion, preguntas=None, grupo=None):
        self.titulo = titulo
        self.fechaCreacion = fechaCreacion
        self.preguntas = preguntas if preguntas else []
        self.grupo = grupo

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def aplicar_a_grupo(self, grupo):
        self.grupo = grupo
        
