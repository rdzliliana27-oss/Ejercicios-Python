#Ejericio de día de la semana

def main():
    print("📅 --- Día de la semana ---")
    numero = int(input("Dame un número del 1 al 7: "))
    dias = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"]

    if 1 <= numero <= 7:
        print(f"✅ El día es {dias[numero - 1]}.")
    else:
        print("❌ El número debe estar entre 1 y 7.")


if __name__ == "__main__":
    main()