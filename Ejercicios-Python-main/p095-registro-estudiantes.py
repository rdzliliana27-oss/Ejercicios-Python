print("Sistema de registro para evento\n")
print("Introduce los nombres y edades (escribe * como nombre para terminar).\n")

nombres = []
edades = []

while True:
    nombre = input("Nombre del asistente: ").strip()
    if nombre == "*":
        break
    if not nombre:
        print("El nombre no puede quedar vacio.")
        continue

    try:
        edad = int(input(f"Edad de {nombre}: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
            continue
        nombres.append(nombre)
        edades.append(edad)
    except ValueError:
        print("Por favor, introduce una edad valida con numeros enteros.")

if not nombres:
    print("\nNo se registraron asistentes.")
else:
    print("\n--- Asistentes mayores de edad ---")
    hay_mayores = False
    for posicion in range(len(nombres)):
        if edades[posicion] >= 18:
            print(f"Nombre: {nombres[posicion]}, edad: {edades[posicion]}")
            hay_mayores = True

    if not hay_mayores:
        print("No hay asistentes mayores de edad.")

    edad_maxima = max(edades)
    posicion_mayor = edades.index(edad_maxima)
    print("\n--- Reconocimiento al asistente de mayor edad ---")
    print(f"{nombres[posicion_mayor]} tiene {edad_maxima} anios.")