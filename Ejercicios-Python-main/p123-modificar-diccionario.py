# Modifica el valor asociado a una clave existente.

colores = {
    "primario": "rojo",
    "secundario": "verde",
    "favorito": "azul",
}

print("Diccionario original:", colores)
clave = input("Que clave quieres modificar? ").strip().lower()

if clave in colores:
    nuevo_color = input("Escribe el nuevo valor: ").strip()
    if nuevo_color:
        colores[clave] = nuevo_color
        print("Diccionario modificado:", colores)
    else:
        print("El nuevo valor no puede quedar vacio.")
else:
    print("Esa clave no existe en el diccionario.")