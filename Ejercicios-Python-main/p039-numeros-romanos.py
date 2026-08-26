#Ejericio de números romanos

def main():
    print("🏛️ --- Conversor a números romanos ---")
    numero = int(input("Dame un número del 1 al 10: "))
    romanos = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

    if 1 <= numero <= 10:
        print(f"✅ El número {numero} en romano es {romanos[numero - 1]}.")
    else:
        print("❌ El número debe estar entre 1 y 10.")


if __name__ == "__main__":
    main()