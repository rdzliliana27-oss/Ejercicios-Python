productos = {
    "agua": 12.00,
    "pan": 15.50,
    "leche": 28.00,
    "huevo": 48.00,
}
carrito = {}

print("Punto de venta")
print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"{producto.title()}: ${precio:.2f}")
print("Escribe el nombre de un producto; deja la entrada vacia para terminar.")

while True:
    nombre = input("Producto: ").strip().lower()
    if not nombre:
        break
    if nombre not in productos:
        print("Producto no encontrado.")
        continue

    try:
        cantidad = int(input(f"Cantidad de {nombre}: "))
    except ValueError:
        print("Error: la cantidad debe ser un numero entero.")
        continue
    if cantidad <= 0:
        print("Error: la cantidad debe ser mayor que cero.")
        continue

    carrito[nombre] = carrito.get(nombre, 0) + cantidad

if not carrito:
    print("No se registraron productos.")
else:
    print("\n--- Ticket ---")
    total = 0
    for nombre, cantidad in carrito.items():
        subtotal = productos[nombre] * cantidad
        total += subtotal
        print(f"{nombre.title()} x {cantidad}: ${subtotal:.2f}")
    print(f"Total: ${total:.2f}")