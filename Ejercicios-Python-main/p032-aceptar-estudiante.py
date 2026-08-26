#Ejericio de aceptar estudiante
# ejercicio que solicita al usuario su nombre, edad y dos calificaciones. El programa verifica si el estudiante es mayor de 18 años y si ambas calificaciones son mayores a 8 para determinar si puede ingresar a la universidad.

def main():
    print("🎓 --- Admisiones de la Universidad Patito ---")
    nombre = input("Dame tu nombre: ")
    edad = int(input("Dame tu edad: "))

    if edad <= 18:
        print(f"❌ Lo sentimos, {nombre}. Solo aceptamos a mayores de 18 años.")
    else:
        print("Ingresa 2 calificaciones para continuar:")
        calificacion1 = float(input())
        calificacion2 = float(input())

        if calificacion1 <= 8 or calificacion2 <= 8:
            print("❌ Se requiere una calificación superior a 8 en ambos exámenes.")
        else:
            print(f"✅ ¡Bienvenid@, {nombre}! Tu edad y tus calificaciones te permiten ingresar.")


if __name__ == "__main__":
    main()