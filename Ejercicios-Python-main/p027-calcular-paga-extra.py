def main():
    print("_________ CALCULAR PAGA EXTRA 💰 _________")

    nombre = input("Nombre del trabajador: ")
    horas = int(input("Horas trabajadas: "))
    paga_por_hora = float(input("Paga por hora: "))

    horas_normales = min(horas, 40)
    horas_extra = max(horas - 40, 0)
    paga_normal = horas_normales * paga_por_hora
    paga_extra = horas_extra * paga_por_hora * 2
    total = paga_normal + paga_extra

    print("✅ Calculo completado.")
    print(f"El trabajador {nombre} trabajo {horas_normales} horas normales y {horas_extra} extra.")
    print(f"💵 Paga normal: ${paga_normal:,.2f}")
    print(f"💵 Paga extra: ${paga_extra:,.2f}")
    print(f"💰 Pago total: ${total:,.2f}")


if __name__ == "__main__":
    main()