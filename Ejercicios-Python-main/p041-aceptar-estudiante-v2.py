#Ejericio de aceptar estudiante versión 2

def main():
    print("🎓 --- Admisiones de la Universidad Kitty Kat SA ---")
    nombre = input("Nombre: ")
    sexo = input("Sexo (h/m): ").strip().lower()
    edad = int(input("Edad: "))
    calificaciones = list(map(float, input("Calificaciones: ").split()))

    promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
    razones = []

    if sexo != "m":
        razones.append("el aspirante debe ser mujer")
    if edad <= 21:
        razones.append("debe ser mayor de 21 años")
    if not 8 <= promedio <= 9.5:
        razones.append("el promedio debe estar entre 8 y 9.5")

    if razones:
        print(f"❌ Estudiante no aceptado: {', '.join(razones)}.")
    else:
        print(f"✅ Estudiante aceptado, {nombre}.")


if __name__ == "__main__":
    main()