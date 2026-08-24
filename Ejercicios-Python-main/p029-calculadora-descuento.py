def main():
    print("_________ CALCULADORA DE DESCUENTO _________")

    compra = float(input("Ingrese el total de su compra: $"))

    if compra > 2000:
        porcentaje = 0.20
    else:
        if compra > 1000:
            porcentaje = 0.10
        else:
            if compra > 500:
                porcentaje = 0.05
            else:
                porcentaje = 0

    descuento = compra * porcentaje
    total = compra - descuento

    print("--- Resumen de la compra ---")
    print(f"Total de la compra: ${compra:,.2f}")
    print(f"Porcentaje de descuento: {int(porcentaje * 100)}%")
    print(f"Ahorro por descuento: ${descuento:,.2f}")
    print(f"Total a pagar: ${total:,.2f}")


if __name__ == "__main__":
    main()