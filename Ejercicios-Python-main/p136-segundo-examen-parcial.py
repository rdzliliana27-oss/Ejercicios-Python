# ==========================================
# FASE 1: INICIALIZACIÓN Y CAPTURA DE DATOS
# ==========================================

# Lista principal (inventario): almacenará un diccionario por cada vuelo registrado.
vuelos = []  

print("AeroRegistro - Sistema de Vuelos")
print("Captura de datos de los vuelos (* para terminar):")

# Bucle infinito controlado para solicitar datos de manera repetitiva.
while True:
    numero_vuelo = input("Número de vuelo: ").strip()

    # Condición de salida: si el usuario deja el campo vacío o escribe "*", el ciclo termina.
    if numero_vuelo == "" or numero_vuelo == "*":
        break

    # Captura del resto de los campos de texto, limpiando espacios con .strip()
    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    aerolinea = input("Aerolínea: ").strip()
    
    # Captura y conversión explícita de tipos de datos numéricos
    pasajeros = int(input("Pasajeros: "))
    tarifa = float(input("Tarifa: "))

    # Estructura de diccionario para agrupar las propiedades del vuelo actual
    vuelo = {
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa,
    }

    # Se añade el diccionario al final de la lista principal de inventario
    vuelos.append(vuelo)

print(f"\nVuelos capturados: {len(vuelos)}")


# ==========================================
# FASE 2: PROCESAMIENTO (SETS Y TUPLAS)
# ==========================================

# 1) Conjunto (Set) de destinos únicos: extrae los destinos evitando duplicados automáticamente.
destinos_unicos = {vuelo["destino"] for vuelo in vuelos}

# 2) Lista de tuplas (Registro histórico inmutable): empaqueta datos clave de cada vuelo.
registro_historico = [
    (vuelo["numero_vuelo"], vuelo["aerolinea"], vuelo["destino"])
    for vuelo in vuelos
]


# ==========================================
# FASE 3: VISUALIZACIÓN Y FORMATO DE SALIDA
# ==========================================

# 1) Despliegue de datos crudos (lista de diccionarios)
print("\nDatos (Lista de diccionarios):")
print(vuelos)

# 2) Despliegue de destinos únicos
print("\nDestinos Únicos (Conjunto):")
print(destinos_unicos)

# 3) Despliegue del registro inmutable
print("\nRegistro Inmutable (Tuplas):")
print(registro_historico)

# 4) Generación de una tabla alineada mediante f-strings
print("\nTabla de datos:")
encabezado = (f"{'No. Vuelo':<10} {'Origen':<15} {'Destino':<15} "
              f"{'Aerolínea':<12} {'Pasajeros':>9} {'Tarifa':>12}")
print(encabezado)
print("-" * len(encabezado))  # Línea separadora adaptada al ancho del encabezado

# Recorrido de la lista para imprimir cada fila formateada (con comas de miles y 2 decimales)
for vuelo in vuelos:
    print(f"{vuelo['numero_vuelo']:<10} {vuelo['origen']:<15} "
          f"{vuelo['destino']:<15} {vuelo['aerolinea']:<12} "
          f"{vuelo['pasajeros']:>9} {vuelo['tarifa']:>12,.2f}")


# ==========================================
# FASE 4: ANALÍTICA Y CÁLCULOS MATEMÁTICOS
# ==========================================

print("\nResumen:")
total_vuelos = len(vuelos)
print(f"Vuelos totales: {total_vuelos}")

# Validación de seguridad: previene errores de división entre cero si no hay registros.
if total_vuelos == 0:
    print("No se registraron vuelos, no hay cálculos que mostrar.")
else:
    # Diccionarios contadores para agrupar frecuencias por aerolínea y destino
    vuelos_por_aerolinea = {}   
    vuelos_por_destino = {}     
    
    # Inicialización de acumuladores y variables de referencia para máximos/mínimos
    suma_pasajeros = 0
    suma_tarifas = 0.0
    vuelo_caro = vuelos[0]      
    vuelo_barato = vuelos[0]

    # Recorrido único para procesar toda la analítica
    for vuelo in vuelos:
        # Contabilizar ocurrencias por aerolínea usando .get(clave, 0) para evitar KeyError
        aerolinea = vuelo["aerolinea"]
        vuelos_por_aerolinea[aerolinea] = vuelos_por_aerolinea.get(aerolinea, 0) + 1

        # Contabilizar ocurrencias por destino
        destino = vuelo["destino"]
        vuelos_por_destino[destino] = vuelos_por_destino.get(destino, 0) + 1

        # Acumulación de valores totales
        suma_pasajeros += vuelo["pasajeros"]
        suma_tarifas += vuelo["tarifa"]

        # Comparación iterativa para identificar el vuelo más caro y el más barato
        if vuelo["tarifa"] > vuelo_caro["tarifa"]:
            vuelo_caro = vuelo
        if vuelo["tarifa"] < vuelo_barato["tarifa"]:
            vuelo_barato = vuelo

    # Cálculo de promedios matemáticos
    promedio_pasajeros = suma_pasajeros / total_vuelos
    promedio_tarifa = suma_tarifas / total_vuelos

    # Impresión estructurada de resultados analíticos
    print("\nAerolíneas:")
    for aerolinea, cantidad in vuelos_por_aerolinea.items():
        print(f"  • {aerolinea}: {cantidad}")

    print("\nDestinos:")
    for destino, cantidad in vuelos_por_destino.items():
        print(f"  • {destino}: {cantidad}")

    print(f"\nPasajeros -> Suma: {suma_pasajeros}, Promedio: {promedio_pasajeros:.2f}")
    print(f"Tarifa -> Suma: ${suma_tarifas:,.2f}, Promedio: ${promedio_tarifa:,.2f}")
    print(f"{vuelo_caro['numero_vuelo']} de ${vuelo_caro['tarifa']:,.2f} es el más caro, "
          f"{vuelo_barato['numero_vuelo']} de ${vuelo_barato['tarifa']:,.2f} es el más barato.")