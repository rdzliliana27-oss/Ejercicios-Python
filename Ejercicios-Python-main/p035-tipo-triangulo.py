#Ejericio de tipo de triángulo
#   ejercicio que solicita al usuario ingresar las longitudes de los tres lados de un triángulo y determina si es equilátero, isósceles o escaleno.

def main():
    print("🔺 --- CLASIFICADOR DE TRIÁNGULOS ---")
    print("Ingresa la longitud de los tres lados de un triángulo.")

    lado_a = float(input("Ingresa la longitud del primer lado: "))
    lado_b = float(input("Ingresa la longitud del segundo lado: "))
    lado_c = float(input("Ingresa la longitud del tercer lado: "))

    if lado_a == lado_b and lado_b == lado_c:
        print("✅ Es un triángulo EQUILÁTERO (todos los lados son iguales).")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("↗️ Es un triángulo ISÓSCELES (al menos dos lados son iguales).")
    else:
        print("❌ Es un triángulo ESCALENO (ningún lado es igual).")


if __name__ == "__main__":
    main()