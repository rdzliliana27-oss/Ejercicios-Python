# p151-promedio-letra.py
# Recibe un promedio y devuelve una letra y un mensaje (tupla)


def calificacion_a_letra(promedio: float) -> tuple[str, str]:
    if 90 <= promedio <= 100:
        return "A", "Excelente"
    if 80 <= promedio < 90:
        return "B", "Bien"
    if 70 <= promedio < 80:
        return "C", "Suficiente"
    if 60 <= promedio < 70:
        return "D", "Deficiente"
    if 0 <= promedio < 60:
        return "F", "Reprobado"
    return "", "Calificación inválida"


def main() -> None:
    promedio = float(input("Introduce el promedio (0-100): "))
    letra, mensaje = calificacion_a_letra(promedio)
    if letra:
        print(f"Calificación: {letra} - {mensaje}")
    else:
        print(mensaje)


if __name__ == "__main__":
    main()
