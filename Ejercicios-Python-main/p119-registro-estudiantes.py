grupo = [
    {"nombre": "Carlos", "edad": 45, "carrera": "Sistemas", "promedio": 9.0},
    {"nombre": "Rocio", "edad": 35, "carrera": "Sistemas", "promedio": 10.0},
]

print("Registro de estudiantes")
print("Ingresa estudiantes. Deja el nombre vacio para terminar.")

while True:
    nombre = input("\nNombre: ").strip()
    if not nombre:
        break

    try:
        edad = int(input("Edad: "))
        promedio = float(input("Promedio: "))
    except ValueError:
        print("Error: edad y promedio deben ser valores numericos.")
        continue

    carrera = input("Carrera: ").strip()
    grupo.append({
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio,
    })

print(f"\nGrupo de estudiantes: {len(grupo)}")
print("-" * 65)
print(f"{'Nombre':<18}{'Edad':<8}{'Carrera':<20}{'Promedio':>10}")
print("-" * 65)
for estudiante in grupo:
    print(
        f"{estudiante['nombre']:<18}"
        f"{estudiante['edad']:<8}"
        f"{estudiante['carrera']:<20}"
        f"{estudiante['promedio']:>10.2f}"
    )

suma_promedios = sum(estudiante["promedio"] for estudiante in grupo)
promedio_grupal = suma_promedios / len(grupo)
print(f"\nSuma de promedios: {suma_promedios:.2f}")
print(f"Promedio general: {promedio_grupal:.2f}")