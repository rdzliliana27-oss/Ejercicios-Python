# Elimina un elemento de una lista con pop o remove.

compras = ["pan", "leche", "huevos", "manzanas"]

print("Lista de compras:", compras)
posicion = int(input("Que posicion quieres eliminar (1-4)? "))

if 1 <= posicion <= len(compras):
    elemento_eliminado = compras.pop(posicion - 1)
    print("Se elimino:", elemento_eliminado)
    print("Lista actualizada:", compras)
else:
    print("Esa posicion no existe en la lista.")

producto = input("\nQue producto quieres quitar por nombre? ")
if producto in compras:
    compras.remove(producto)
    print("Lista despues de remove:", compras)
else:
    print("Ese producto no esta en la lista.")