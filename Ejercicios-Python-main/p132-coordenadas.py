# Registra y consulta coordenadas usando tuplas.

zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

print("--- Coordenadas ---")
print("Tipo:", type(zacatecas))
print("Ciudad:", zacatecas[0])
print("Latitud:", zacatecas[1])
print("Longitud:", zacatecas[-1])

nombre, latitud, longitud = zacatecas
print(f"{nombre}: ({latitud}, {longitud})")

print("\n--- Ubicaciones ---")
for lugar in (zacatecas, guadalupe):
    print(lugar[0], "->", lugar[1:])

_, latitud_zacatecas, longitud_zacatecas = zacatecas
_, latitud_guadalupe, longitud_guadalupe = guadalupe
centro = (
    (latitud_zacatecas + latitud_guadalupe) / 2,
    (longitud_zacatecas + longitud_guadalupe) / 2,
)
print("\nPunto medio:", centro)
print('"Zacatecas" esta en sus coordenadas:', "Zacatecas" in zacatecas)

ampliada = zacatecas + ("ZAC",)
print("Tupla ampliada:", ampliada)
print("Tupla original:", zacatecas)