print("🐱 Resumen de ventas 🐱")
print("  /\\_/\\")
print(" ( o.o )\n")

ventas = [250, 800, 1200, 450, 1800, 950]
finales = [
    round(venta * 0.90, 2) if venta > 1000 else venta
    for venta in ventas
]
relevantes = [venta for venta in finales if venta > 500]

print(f"Ventas originales: {ventas}")
print(f"Ventas finales: {finales}")
print(f"Ventas mayores de $500: {relevantes}")
print(f"Total relevante: ${sum(relevantes):.2f}")