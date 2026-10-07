frase = input("Ingresa una frase: ")

try:
    longitud_minima = int(input("Longitud minima de las palabras: "))
except ValueError:
    print("Error: la longitud debe ser un numero entero.")
else:
    if longitud_minima < 0:
        print("Error: la longitud no puede ser negativa.")
    else:
        palabras = frase.split()
        filtradas = [palabra for palabra in palabras if len(palabra) >= longitud_minima]
        print(f"Palabras originales: {palabras}")
        print(f"Palabras con al menos {longitud_minima} caracteres: {filtradas}")