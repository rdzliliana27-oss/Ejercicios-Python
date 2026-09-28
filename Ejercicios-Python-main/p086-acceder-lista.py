# Accede a los elementos de una lista usando su indice.

frutas = ["manzana", "pera", "uva", "naranja"]

print("Lista de frutas:", frutas)
print("Primer elemento:", frutas[0])
print("Tercer elemento:", frutas[2])
print("Ultimo elemento:", frutas[-1])

indice = int(input("\nQue posicion quieres consultar (1-4)? "))

if 1 <= indice <= len(frutas):
    print("En esa posicion esta:", frutas[indice - 1])
else:
    print("Esa posicion no existe en la lista.")