# Agrega una nueva clave y su valor a un diccionario.

animales = {
    "mascota": "perro",
    "granja": "vaca",
    "selva": "jaguar",
}

print("Diccionario original:", animales)
clave = input("Nueva clave: ").strip().lower()
valor = input("Valor para esa clave: ").strip()

if not clave or not valor:
    print("La clave y el valor no pueden quedar vacios.")
elif clave in animales:
    print("Esa clave ya existe. Usa modificar-diccionario para cambiar su valor.")
else:
    animales[clave] = valor
    print("Diccionario actualizado:", animales)