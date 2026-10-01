print("Analisis de precios de acciones\n")

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
precios = [150.25, 152.50, 149.75, 155.00, 153.20]

precio_maximo = max(precios)
precio_minimo = min(precios)
posicion_maxima = precios.index(precio_maximo)
posicion_minima = precios.index(precio_minimo)

print(f"Precios de cierre de la semana: {precios}")
print(f"El precio mas alto fue ${precio_maximo:.2f} el dia {dias[posicion_maxima]}.")
print(f"El precio mas bajo fue ${precio_minimo:.2f} el dia {dias[posicion_minima]}.")