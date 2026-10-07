print("Procesador de notas")

try:
    notas = [float(valor) for valor in input("Ingresa las notas (0 a 10), separadas por espacios: ").split()]
except ValueError:
    print("Error: ingresa solamente valores numericos.")
else:
    if not notas:
        print("No se ingresaron notas.")
    elif any(nota < 0 or nota > 10 for nota in notas):
        print("Error: cada nota debe estar entre 0 y 10.")
    else:
        promedio = sum(notas) / len(notas)
        aprobadas = [nota for nota in notas if nota >= 6]

        print(f"Notas: {notas}")
        print(f"Cantidad de notas: {len(notas)}")
        print(f"Suma: {sum(notas):.2f}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Nota mas alta: {max(notas):.2f}")
        print(f"Nota mas baja: {min(notas):.2f}")
        print(f"Notas aprobatorias (6 o mas): {aprobadas}")