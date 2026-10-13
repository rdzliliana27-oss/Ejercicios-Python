# Cuenta cuantas veces aparece cada caracter en un texto.

texto = input("Escribe una frase: ").lower()
conteo = {}

for caracter in texto:
    if caracter in conteo:
        conteo[caracter] += 1
    else:
        conteo[caracter] = 1

print("\nFrecuencia de caracteres:")
for caracter, cantidad in conteo.items():
    etiqueta = "[espacio]" if caracter == " " else caracter
    print(f"{etiqueta}: {cantidad}")

print(f"\nTotal de caracteres: {len(texto)}")
print(f"Caracteres distintos: {len(conteo)}")