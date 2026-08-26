#Ejericio de número mayor

def main():
    print("🏆 --- Buscador del número mayor ---")
    numeros = list(map(int, input("Dame tres números: ").split()))

    if len(numeros) != 3:
        print("❌ Debes ingresar exactamente tres números.")
        return

    print(f"✅ El mayor es {max(numeros)}.")


if __name__ == "__main__":
    main()