# models/usuario.py
class Usuario:
    def __init__(self, id, nombre, email, edad, sexo):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.sexo = sexo

    def __str__(self):
        return f"{self.id}: {self.nombre}, {self.email}, {self.edad}, {self.sexo}"
