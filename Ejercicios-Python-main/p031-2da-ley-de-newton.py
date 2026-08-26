#Ejericio de la segunda ley de Newton
# ejercicio que solicita al usuario elegir entre calcular la fuerza, la masa o la aceleración según la segunda ley de Newton (fuerza = masa * aceleración).

def main():
    print("⚙️ --- Calculadora de la 2da Ley de Newton ---")
    print("[1] 💪 Calcular la Fuerza (fuerza = masa * aceleración)")
    print("[2] ⚖️ Calcular la Masa (masa = fuerza / aceleración)")
    print("[3] 🚀 Calcular la Aceleración (aceleración = fuerza / masa)")

    opcion = int(input("Elige una opción (1, 2 o 3): "))

    if opcion == 1:
        masa = float(input("Dame la masa: "))
        aceleracion = float(input("Dame la aceleración: "))
        print(f"✅ La fuerza es: {masa * aceleracion}")
    elif opcion == 2:
        fuerza = float(input("Dame la fuerza: "))
        aceleracion = float(input("Dame la aceleración: "))
        print(f"✅ La masa es: {fuerza / aceleracion}")
    elif opcion == 3:
        fuerza = float(input("Dame la fuerza: "))
        masa = float(input("Dame la masa: "))
        print(f"✅ La aceleración es: {fuerza / masa}")
    else:
        print("❌ Opción inválida. Por favor, elige 1, 2 o 3.")


if __name__ == "__main__":
    main()