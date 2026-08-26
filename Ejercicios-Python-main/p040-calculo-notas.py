#Ejericio de cálculo de notas

def main():
    print("📝 --- Cálculo del promedio de notas ---")
    calificaciones = list(map(float, input("Ingresa 5 calificaciones: ").split()))

    if len(calificaciones) != 5:
        print("❌ Debes ingresar exactamente 5 calificaciones.")
        return
    if any(calificacion < 0 or calificacion > 10 for calificacion in calificaciones):
        print("❌ Las calificaciones deben estar entre 0 y 10.")
        return

    promedio = sum(calificaciones) / 5
    print(f"📊 Promedio: {promedio:.1f}")

    if promedio < 6:
        print("❌ Quedas reprobado")
    elif promedio < 7:
        print("🟡 Pasas de panzazo")
    elif promedio < 8:
        print("👍 Muy bien, puedes mejorar")
    elif promedio < 9:
        print("🌟 Excelente, sigue así")
    else:
        print("🏅 Perfecto, tu esfuerzo valió la pena")


if __name__ == "__main__":
    main()