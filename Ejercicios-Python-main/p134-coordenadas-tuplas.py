# Practica tuplas con coordenadas de ciudades.

GATO = r"""
    /\_/\\
    ( o.o )  Coordenadas con tuplas
    > ^ <
    """

zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

print(GATO)
print("=" * 48)
print("             TAREA 8 - TUPLAS")
print("=" * 48)

print("\n--- Tuplas y tipo de dato ---")
print(f"Tupla Zacatecas: {zacatecas}, Tipo: {type(zacatecas)}")
print(f"Tupla Guadalupe: {guadalupe}, Tipo: {type(guadalupe)}")

print("\n--- Acceso por indices: Zacatecas ---")
print(
    f"Positivos -> Nombre: {zacatecas[0]}, "
    f"Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}"
)
print(
    f"Negativos -> Nombre: {zacatecas[-3]}, "
    f"Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}"
)

print("\n--- Desempaquetado ---")
for ubicacion in (zacatecas, guadalupe):
    nombre, latitud, longitud = ubicacion
    print(f"{nombre}: ({latitud}, {longitud})")

print("\n--- Recorrido y slicing ---")
for ubicacion in (zacatecas, guadalupe):
    nombre = ubicacion[0]
    coordenadas = ubicacion[1:]
    print(f"Ubicacion: {nombre}, Coordenadas: {coordenadas}")

latitud_media = (zacatecas[1] + guadalupe[1]) / 2
longitud_media = (zacatecas[2] + guadalupe[2]) / 2
print("\n--- Punto medio aproximado ---")
print(f"Punto medio aproximado: ({latitud_media:.2f}, {longitud_media:.2f})")

nueva_zacatecas = zacatecas + ("ZAC",)
print("\n--- Tupla ampliada ---")
print(f"Nueva tupla Zacatecas: {nueva_zacatecas}")
print(f"Original sin cambios: {zacatecas}")

print("\n--- Pertenencia e inmutabilidad ---")
print(f"'Zacatecas' pertenece a la tupla: {'Zacatecas' in zacatecas}")
print(
    "Nota: intentar reemplazar un elemento directamente arroja TypeError "
    "porque las tuplas son inmutables."
)