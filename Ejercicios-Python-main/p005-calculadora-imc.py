# Calculadora de IMC
# Fórmula: IMC = peso / altura^2


def calcular_imc(peso: float, altura: float) -> float:
    if peso <= 0 or altura <= 0:
        raise ValueError("El peso y la altura deben ser mayores que 0.")
    return peso / (altura ** 2)


def clasificar_imc(imc: float) -> str:
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    return "Obesidad"


def main() -> None:
    try:
        peso = float(input("Ingrese su peso en kg: "))
        altura = float(input("Ingrese su altura en metros: "))

        imc = calcular_imc(peso, altura)
        categoria = clasificar_imc(imc)

        print(f"Su IMC es: {imc:.2f}")
        print(f"Clasificación: {categoria}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
