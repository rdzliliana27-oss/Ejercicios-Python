def main():
    print("_________ RETIRO DE CUENTA _________")

    saldo_actual = 1500.50
    print(f"Tu saldo actual es: ${saldo_actual:,.2f}")
    cantidad_retiro = float(input("Ingrese la cantidad a retirar: $"))

    if cantidad_retiro > 0:
        if cantidad_retiro <= saldo_actual:
            nuevo_saldo = saldo_actual - cantidad_retiro
            print("Retiro exitoso.")
            print(f"Tu nuevo saldo es: ${nuevo_saldo:,.2f}")
        else:
            print("Fondos insuficientes. No se puede completar la transaccion.")
    else:
        print("La cantidad a retirar debe ser un numero positivo.")

    print("Gracias por usar nuestro servicio.")


if __name__ == "__main__":
    main()