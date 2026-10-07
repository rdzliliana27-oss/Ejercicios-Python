meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]
dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    dia = int(input("Ingresa el dia: "))
    numero_mes = int(input("Ingresa el numero del mes (1 a 12): "))
except ValueError:
    print("Error: el dia y el mes deben ser numeros enteros.")
else:
    if not 1 <= numero_mes <= 12:
        print("Error: el mes debe estar entre 1 y 12.")
    elif not 1 <= dia <= dias_por_mes[numero_mes - 1]:
        print("Error: ese dia no existe en el mes indicado.")
    else:
        print(f"Fecha: {dia} de {meses[numero_mes - 1]}")