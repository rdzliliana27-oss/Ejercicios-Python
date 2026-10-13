# Elimina un elemento de un diccionario usando su clave.

compras = {
    "pan": 18.50,
    "leche": 27.00,
    "huevos": 42.00,
    "manzanas": 30.00,
}

print("Lista de compras:", compras)
clave = input("Que producto quieres eliminar? ").strip().lower()

if clave in compras:
    valor_eliminado = compras.pop(clave)
    print(f"Se elimino {clave}: ${valor_eliminado:.2f}")
    print("Diccionario actualizado:", compras)
else:
    print("Esa clave no existe en el diccionario.")