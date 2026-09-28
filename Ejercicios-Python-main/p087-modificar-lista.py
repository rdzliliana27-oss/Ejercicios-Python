# Cambia el valor de un elemento usando su indice.

colores = ["rojo", "azul", "verde", "amarillo"]

print("Colores originales:", colores)
indice = int(input("Que posicion quieres cambiar (1-4)? "))

if 1 <= indice <= len(colores):
    nuevo_color = input("Escribe el nuevo color: ")
    colores[indice - 1] = nuevo_color
    print("Colores modificados:", colores)
else:
    print("Esa posicion no existe en la lista.")