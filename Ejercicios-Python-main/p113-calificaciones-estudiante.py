print("Calificaciones del estudiante")

try:
    cantidad = int(input("Cuantas materias vas a registrar? "))
except ValueError:
    print("Error: ingresa una cantidad entera positiva.")
else:
    if cantidad <= 0:
        print("Error: registra al menos una materia.")
    else:
        calificaciones = {}
        for indice in range(cantidad):
            materia = input(f"Nombre de la materia {indice + 1}: ").strip()
            if not materia:
                print("Error: el nombre de la materia no puede estar vacio.")
                break
            if materia in calificaciones:
                print("Error: no repitas el nombre de una materia.")
                break

            try:
                nota = float(input(f"Calificacion de {materia} (0 a 10): "))
            except ValueError:
                print("Error: la calificacion debe ser numerica.")
                break
            if not 0 <= nota <= 10:
                print("Error: la calificacion debe estar entre 0 y 10.")
                break
            calificaciones[materia] = nota
        else:
            promedio = sum(calificaciones.values()) / len(calificaciones)
            print("\nCalificaciones:")
            for materia, nota in calificaciones.items():
                print(f"{materia}: {nota:.2f}")
            print(f"Promedio: {promedio:.2f}")