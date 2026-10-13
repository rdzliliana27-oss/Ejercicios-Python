# Crea un diccionario y accede a sus valores usando las claves.

estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Computacion",
    "promedio": 9.4,
}

print("Datos del estudiante:", estudiante)
print("Nombre:", estudiante["nombre"])
print("Carrera:", estudiante["carrera"])

clave = input("\nQue dato quieres consultar? ").strip().lower()
if clave in estudiante:
    print(f"{clave.title()}: {estudiante[clave]}")
else:
    print("Esa clave no existe en el diccionario.")