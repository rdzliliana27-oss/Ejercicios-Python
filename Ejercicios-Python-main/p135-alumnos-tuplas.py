# Practica tuplas anidadas con un registro escolar.
# Se registran alumnos, carreras y calificaciones, y se calculan promedios.

GATO = r"""
    /\_/\\
    ( -.- )  Registro escolar con tuplas
    > ^ <
    """

alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Mar", "ISC", (10, 9, 10, 10)),
)

print(GATO)
print("=" * 52)
print("          TAREA 8 - REGISTRO ESCOLAR")
print("=" * 52)

print("\n--- Registro original ---")
print(f"Registros de alumnos: {alumnos}")
print(f"Total de alumnos: {len(alumnos)}")

promedios = []
print("\n--- Promedios ---")
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    promedios.append((nombre, promedio))
    print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")

promedios = tuple(promedios)
mejor_nombre, mejor_promedio = max(promedios, key=lambda par: par[1])
print("\n--- Resumen de promedios ---")
print(f"Pares (nombre, promedio): {promedios}")
print(f"Alumno con mejor promedio: {mejor_nombre} con {mejor_promedio:.2f}")

print("\n--- Consultas de calificaciones ---")
for nombre, _, calificaciones in alumnos:
    cantidad_diez = calificaciones.count(10)
    indice_primera = calificaciones.index(calificaciones[0])
    print(
        f"{nombre} -> Conteo de 10s: {cantidad_diez}, "
        f"Indice de primera calificacion: {indice_primera}"
    )

ordenados = tuple(sorted(promedios, key=lambda par: par[1]))
print("\n--- Orden por promedio ---")
print(f"Ordenados por promedio: {ordenados}")

eva = ("Eva", "ISC", (9, 9, 10))
alumnos_con_eva = alumnos + (eva,)
print("\n--- Nueva alumna ---")
print(f"Tupla original intacta: {alumnos}")
print(f"Nueva tupla con Eva: {alumnos_con_eva}")