print("🐱 Aplanar una matriz 🐱")
print("  /\\_/\\")
print(" ( o.o )\n")

matriz = [[4, -2, 8], [0, 5, -1], [7, 3, -6]]
valores = [numero for fila in matriz for numero in fila]
positivos = [
    numero
    for fila in matriz
    for numero in fila
    if numero > 0
]

print(f"Matriz: {matriz}")
print(f"Lista plana: {valores}")
print(f"Valores positivos: {positivos}")