#Ejericio de precio de entrada al cine

def main():
    print("🎬 --- Taquilla del cine ---")
    edad = int(input("Edad del cliente: "))

    if edad < 0:
        print("❌ La edad no puede ser negativa.")
    elif edad < 5:
        print("🎟️ Entra gratis.")
    elif edad <= 12:
        print("🎟️ El precio de la entrada es $5.")
    elif edad <= 64:
        print("🎟️ El precio de la entrada es $10.")
    else:
        print("🎟️ El precio de la entrada es $7.")


if __name__ == "__main__":
    main()