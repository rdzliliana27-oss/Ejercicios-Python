# Practica operaciones y pertenencia con conjuntos de numeros.

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

print("--- Conjuntos base ---")
print("A:", A)
print("B:", B)
print("C:", C)

print("\n--- Operaciones ---")
print("Union (A | B):", A | B)
print("Union (B | C):", B | C)
print("Diferencia (A - C):", A - C)
print("Diferencia simetrica (B ^ C):", B ^ C)
print("Interseccion (B & C):", B & C)

print("\n--- Afirmaciones ---")
print("¿A es subconjunto de B?:", A <= B)
print("¿C es subconjunto de A?:", C <= A)
print("¿El numero 100 esta en A?:", 100 in A)
print("¿El numero 60 esta en A, B y C?:", 60 in A and 60 in B and 60 in C)
print("¿El numero 900 no esta en C?:", 900 not in C)