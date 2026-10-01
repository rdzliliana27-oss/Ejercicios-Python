print("--- Calculo del producto punto ---\n")

vector_a = [1, 3, -5]
vector_b = [4, -2, -1]

print(f"Vector A: {vector_a}")
print(f"Vector B: {vector_b}\n")

if len(vector_a) != len(vector_b):
    print("Error: los vectores deben tener la misma longitud.")
else:
    producto_punto = 0
    for posicion in range(len(vector_a)):
        producto_punto += vector_a[posicion] * vector_b[posicion]

    print(f"El producto punto de los vectores es: {producto_punto}")