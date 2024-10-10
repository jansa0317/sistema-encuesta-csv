from models.pregunta import Pregunta
from models.usuario import Usuario

class Respuesta:
    def __init__(self, pregunta: Pregunta, usuario: Usuario, valor):
        self.pregunta = pregunta
        self.usuario = usuario
        self.valor = valor
