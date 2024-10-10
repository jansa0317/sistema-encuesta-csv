# app.py
import csv
from models.usuario import Usuario
from models.encuesta import Encuesta, Pregunta, Grupo

def cargar_usuarios_de_csv(archivo_csv):
    usuarios = {}
    with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            id_usuario = row[0]
            nombre = row[1]
            email = row[2]
            edad = row[3]
            sexo = row[4]
            # Crear usuario con los datos del CSV
            usuarios[id_usuario] = Usuario(id_usuario, nombre, email, edad, sexo)
    return usuarios

def realizar_encuesta(usuario):
    print(f"\nRealizando encuesta para: {usuario.nombre}\n")
    # Aquí puedes definir las preguntas de la encuesta
    preguntas = [
        Pregunta(texto="¿Cómo calificaría el servicio?"),
        Pregunta(texto="¿Recomendaría el servicio?"),
    ]
    
    respuestas = []
    for pregunta in preguntas:
        respuesta = input(f"{pregunta.texto} ")
        respuestas.append(respuesta)
    
    # Aquí puedes crear y guardar la encuesta si es necesario
    encuesta = Encuesta(titulo="Encuesta de Satisfacción", fechaCreacion="2024-10-03", preguntas=preguntas)
    print("\nEncuesta completada. Resultados:")
    for pregunta, respuesta in zip(preguntas, respuestas):
        print(f"{pregunta.texto} - Respuesta: {respuesta}")

def main():
    usuarios = cargar_usuarios_de_csv('data/usuarios.csv')
    print("Usuarios cargados:")
    for usuario in usuarios.values():
        print(usuario)

    id_usuario = input("\nIngrese el ID del usuario para la encuesta: ")
    
    # Verificar si el ID del usuario existe
    if id_usuario in usuarios:
        usuario_seleccionado = usuarios[id_usuario]
        realizar_encuesta(usuario_seleccionado)
    else:
        print("ID de usuario no encontrado.")

if __name__ == "__main__":
    main()
