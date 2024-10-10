import csv

def cargar_usuarios_desde_csv(archivo_csv):
    usuarios = []
    with open(archivo_csv, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuario = Usuario(nombre=row['nombre'], email=row['email'])
            usuarios.append(usuario)
    return usuarios
