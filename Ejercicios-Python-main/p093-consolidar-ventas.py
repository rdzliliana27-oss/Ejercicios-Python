print("Consolidar ventas de dos sucursales\n")

while True:
    try:
        cantidad_dias = int(input("Cuantas ventas diarias se registraran? "))
        if cantidad_dias > 0:
            break
        print("Introduce una cantidad mayor que cero.")
    except ValueError:
        print("Entrada no valida. Introduce un numero entero.")

ventas_sucursal_1 = []
ventas_sucursal_2 = []

print("\nRegistrando ventas de la sucursal 1:")
for dia in range(cantidad_dias):
    venta = float(input(f"Venta del dia {dia + 1}: "))
    ventas_sucursal_1.append(venta)

print("\nRegistrando ventas de la sucursal 2:")
for dia in range(cantidad_dias):
    venta = float(input(f"Venta del dia {dia + 1}: "))
    ventas_sucursal_2.append(venta)

ventas_consolidadas = []
for dia in range(cantidad_dias):
    total_dia = ventas_sucursal_1[dia] + ventas_sucursal_2[dia]
    ventas_consolidadas.append(total_dia)

print("\n--- Reporte de ventas ---")
print(f"Sucursal 1: {ventas_sucursal_1}")
print(f"Sucursal 2: {ventas_sucursal_2}")
print(f"Ventas consolidadas: {ventas_consolidadas}")