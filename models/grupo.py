class Grupo:
    def __init__(self, nombre, criterios=None):
        self.nombre = nombre
        self.criterios = criterios if criterios else {}

    def __repr__(self):
        return f'Grupo(nombre="{self.nombre}", criterios={self.criterios})'
