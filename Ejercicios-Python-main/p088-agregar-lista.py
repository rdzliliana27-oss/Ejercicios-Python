# Agrega elementos al final o en una posicion especifica de una lista.

animales = ["perro", "gato", "conejo"]

print("Lista original:", animales)
nuevo_animal = input("Que animal quieres agregar? ")
animales.append(nuevo_animal)
print("Despues de append:", animales)

posicion = int(input("En que posicion quieres insertar otro animal (1-4)? "))
if 1 <= posicion <= len(animales) + 1:
    otro_animal = input("Escribe el otro animal: ")
    animales.insert(posicion - 1, otro_animal)
    print("Despues de insert:", animales)
else:
    print("Esa posicion no es valida.")