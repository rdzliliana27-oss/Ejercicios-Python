#Ejericio de números consecutivos

def main():
    print("🔢 --- Verificador de números consecutivos ---")
    numeros = list(map(int, input("Dame tres números: ").split()))

    if len(numeros) != 3:
        print("❌ Debes ingresar exactamente tres números.")
        return

    ordenados = sorted(numeros)
    if ordenados[1] == ordenados[0] + 1 and ordenados[2] == ordenados[1] + 1:
        print(f"✅ Los números {numeros[0]}, {numeros[1]}, {numeros[2]} son consecutivos.")
    else:
        print(f"❌ Los números {numeros[0]}, {numeros[1]}, {numeros[2]} no son consecutivos.")


if __name__ == "__main__":
    main()