print("Reporte de ventas")

try:
    cantidad_compras = int(input("Numero de compras a registrar: "))
except ValueError:
    print("Error: debes ingresar un numero entero.")
    raise SystemExit

compras = []
for numero in range(1, cantidad_compras + 1):
    print(f"\n--- Compra {numero} ---")
    cliente = input("Nombre del cliente: ").strip()
    producto = input("Nombre del producto: ").strip()

    try:
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
    except ValueError:
        print("Error: cantidad y precio deben ser valores numericos. Compra omitida.")
        continue

    compras.append({
        "cliente": cliente,
        "producto": producto,
        "cantidad": cantidad,
        "precio": precio,
    })

clientes = {}
for compra in compras:
    nombre_cliente = compra["cliente"]
    if nombre_cliente not in clientes:
        clientes[nombre_cliente] = {"cantidad": 0, "subtotal": 0.0}

    clientes[nombre_cliente]["cantidad"] += compra["cantidad"]
    clientes[nombre_cliente]["subtotal"] += compra["cantidad"] * compra["precio"]

print("\n--- Compras registradas ---")
for compra in compras:
    print(compra)

print("\n--- Totales por cliente ---")
if not clientes:
    print("No se registraron compras.")
else:
    for nombre_cliente, datos in clientes.items():
        print(f"Cliente: {nombre_cliente}")
        print(f"Cantidad total de productos: {datos['cantidad']}")
        print(f"Subtotal a pagar: ${datos['subtotal']:.2f}\n")