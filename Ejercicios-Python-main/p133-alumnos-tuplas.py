# Registra alumnos y calificaciones usando tuplas anidadas.

alumnos = (
    ("Ana", "ISC", (9, 10, 9)),
    ("Luis", "ISW", (8, 8, 9)),
    ("Mar", "ISC", (10, 9, 10)),
)

print("--- Registro escolar ---")
print("Total de alumnos:", len(alumnos))

for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{nombre} ({carrera}): {promedio:.2f}")

print("\nPrimera persona:", alumnos[0][0])
print("Calificaciones de Mar:", alumnos[-1][2])

promedios = tuple(
    (nombre, sum(calificaciones) / len(calificaciones))
    for nombre, _, calificaciones in alumnos
)
print("Promedios:", promedios)

mejor_promedio = max(promedios, key=lambda alumno: alumno[1])
print("Mayor promedio:", mejor_promedio)

nombres = tuple(alumno[0] for alumno in alumnos)
print("Nombres:", nombres)