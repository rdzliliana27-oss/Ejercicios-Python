# Recorre un diccionario de calificaciones y calcula suma y promedio.

calificaciones = {
    "Matematicas": 9,
    "Ciencias": 8,
    "Historia": 10,
    "Ingles": 7,
}

print("Calificaciones:")
suma = 0
for materia, calificacion in calificaciones.items():
    print(f"{materia}: {calificacion}")
    suma += calificacion

promedio = suma / len(calificaciones)
print(f"\nTotal de materias: {len(calificaciones)}")
print(f"Suma de calificaciones: {suma}")
print(f"Promedio: {promedio:.2f}")