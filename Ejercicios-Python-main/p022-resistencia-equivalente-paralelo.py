def main():
    print("===== RESISTENCIA EQUIVALENTE EN PARALELO =====")

    resistencias = []
    for numero in range(1, 5):
        resistencia = float(input(f"Ingrese el valor de R{numero}: "))
        if resistencia <= 0:
            print("Todas las resistencias deben ser mayores que 0.")
            return
        resistencias.append(resistencia)

    resistencia_equivalente = 1 / sum(1 / resistencia for resistencia in resistencias)
    print(f"La resistencia equivalente es: {resistencia_equivalente:.2f} ohmios")


if __name__ == "__main__":
    main()
