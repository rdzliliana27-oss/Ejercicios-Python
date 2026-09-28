# Recorre una lista con un ciclo for.

calificaciones = [9, 8, 10, 7, 9]
suma = 0

print("Calificaciones:")
for posicion, calificacion in enumerate(calificaciones, start=1):
    print(f"Calificacion {posicion}: {calificacion}")
    suma = suma + calificacion

promedio = suma / len(calificaciones)
print("Suma:", suma)
print("Promedio:", promedio)