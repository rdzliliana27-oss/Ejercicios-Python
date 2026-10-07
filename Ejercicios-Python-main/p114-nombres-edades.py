print("Registro de nombres y edades")

try:
    cantidad = int(input("Cuantas personas quieres registrar? "))
except ValueError:
    print("Error: ingresa una cantidad entera no negativa.")
else:
    if cantidad < 0:
        print("Error: la cantidad no puede ser negativa.")
    else:
        personas = {}
        for indice in range(cantidad):
            nombre = input(f"Nombre {indice + 1}: ").strip()
            if not nombre:
                print("Error: el nombre no puede estar vacio.")
                break
            if nombre in personas:
                print("Error: ese nombre ya fue registrado.")
                break

            try:
                edad = int(input(f"Edad de {nombre}: "))
            except ValueError:
                print("Error: la edad debe ser un numero entero.")
                break
            if edad < 0:
                print("Error: la edad no puede ser negativa.")
                break
            personas[nombre] = edad
        else:
            print("\nPersonas registradas:")
            for nombre, edad in personas.items():
                print(f"{nombre}: {edad} anios")

            if personas:
                promedio = sum(personas.values()) / len(personas)
                print(f"Edad promedio: {promedio:.1f} anios")