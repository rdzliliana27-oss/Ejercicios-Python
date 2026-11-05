# p147-estacion-año.py
# Dado un número de mes, regresa el nombre de la estación del año


def estacion_ano(mes: int) -> str:
    if mes in [12, 1, 2]:
        return "Invierno"
    if mes in [3, 4, 5]:
        return "Primavera"
    if mes in [6, 7, 8]:
        return "Verano"
    if mes in [9, 10, 11]:
        return "Otoño"
    return "Mes inválido"


print("Dame un número de mes (1-12):")
mes = int(input())
print(f"La estación del año para el mes {mes} es: {estacion_ano(mes)}")
