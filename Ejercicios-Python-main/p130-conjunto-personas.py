# Practica operaciones y pertenencia con conjuntos de nombres.

lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista1)
B = set(lista2)

print("--- Conjuntos base ---")
print("A:", A)
print("B:", B)

print("\n--- Operaciones ---")
print("Union (A | B):", A | B)
print("Interseccion (A & B):", A & B)
print("Diferencia (A - B):", A - B)
print("Diferencia simetrica (A ^ B):", A ^ B)

print("\n--- Afirmaciones ---")
print("¿{Pablo, Mateo} es subconjunto de B?:", {"Pablo", "Mateo"} <= B)
print("¿A es superconjunto de {Reynaldo, Angelica}?:", A >= {"Reynaldo", "Angelica"})
print('¿"Pedro" esta en A?:', "Pedro" in A)
print('¿"Lilia" no esta en B?:', "Lilia" not in B)