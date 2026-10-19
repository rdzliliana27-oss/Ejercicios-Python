# Gestion de un padron municipal usando conjuntos.

municipios = {
    "Zacatecas",
    "Guadalupe",
    "Jerez",
    "Fresnillo",
    "Fresnillo",
}

print("--- Gestion de Municipios (con Conjuntos) ---\n")
print(f"La coleccion es del tipo: {type(municipios)}")
print(f"Longitud del padron: {len(municipios)}")
print(f"Padron original: {municipios}\n")

print("Municipios registrados:")
for municipio in municipios:
    print(municipio, end=" | ")

print(f"\n\n¿Esta Zacatecas en el padron?: {'Zacatecas' in municipios}")

print("\n--- Altas en el Padron ---")
municipios.add("Teul")
print(f"Alta con add() (Teul):\n{municipios}\n")

otros_municipios = {"Luis Moya", "Ojocaliente", "Tepetongo"}
municipios.update(otros_municipios)
print(f"Alta con update() (varios):\n{municipios}\n")

print("--- Bajas del Padron ---")
municipios.remove("Zacatecas")
print(f"Baja con remove() (Zacatecas):\n{municipios}\n")

municipios.discard("Ojocaliente")
print(f"Baja con discard() (Ojocaliente):\n{municipios}\n")

municipio_eliminado = municipios.pop()
print(
    "Baja con pop() (elemento arbitrario):\n"
    f"{municipios}\nEliminado: {municipio_eliminado}\n"
)

municipios.clear()
print(f"Padron vaciado con clear():\n{municipios}")