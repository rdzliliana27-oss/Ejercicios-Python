print("Procesador de calificaciones de un curso\n")
print("Introduce calificaciones entre 0 y 10 (usa 99 para terminar).\n")

calificaciones = []

while True:
    try:
        calificacion = float(input("Calificacion > "))
        if calificacion == 99:
            break
        if 0 <= calificacion <= 10:
            calificaciones.append(calificacion)
        else:
            print("Error: la calificacion debe estar entre 0 y 10.")
    except ValueError:
        print("Entrada no valida. Por favor, introduce un numero.")

if not calificaciones:
    print("No se ingresaron calificaciones.")
else:
    suma = sum(calificaciones)
    promedio = suma / len(calificaciones)
    mayores_promedio = [calificacion for calificacion in calificaciones if calificacion > promedio]

    print(f"\nSe capturaron {len(calificaciones)} calificaciones.")
    print(f"Las calificaciones son: {calificaciones}")
    print("\n--- Estadisticas del curso ---")
    print(f"Suma total: {suma}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Calificaciones mayores al promedio: {len(mayores_promedio)} -> {mayores_promedio}")
    print(f"Calificacion mas alta: {max(calificaciones)}")
    print(f"Calificacion mas baja: {min(calificaciones)}")