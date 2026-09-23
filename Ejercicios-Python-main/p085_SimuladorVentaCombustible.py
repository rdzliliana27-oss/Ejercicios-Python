"""
p085_SimuladorVentaCombustible.py
Examen Practico Complementario - Programacion Python
Computacion Aplicada

Sistema interactivo de consola para la gestion de una estacion de servicio.
Restriccion estricta del examen: NO se usan listas, tuplas, diccionarios
ni funciones personalizadas (def). Solo se usan los elementos vistos en
el Bloque 1: variables, tipos de datos, operadores, condicionales y ciclos.
segun las inscriccion del examen, el sistema debe incluir las siguientes funcionalidades:
1. Venta de Combustible: Calcula el total a pagar por un cliente segun el tipo de combustible, precio por litro y cantidad de litros cargados.
2. Simulacion de Rendimiento: Proyecta el rendimiento de un vehiculo en kilometros y litros consumidos durante un periodo de meses, considerando el kilometraje inicial, rendimiento del vehiculo y kilometros recorridos por mes.
3. Clasificador de Cliente: Clasifica a un cliente segun su volumen de compra mensual en litros y asigna un descuento correspondiente.
4. Salir: Finaliza la ejecucion del programa y muestra un mensaje de despedida.
"""

# ============================================================
# CICLO PRINCIPAL DEL MENU
# ============================================================
while True:

    print("\n" + "=" * 45)
    print(f"{'ESTACION DE SERVICIO - MENU PRINCIPAL':^45}")
    print("=" * 45)
    print("1. Venta de Combustible")
    print("2. Simulacion de Rendimiento")
    print("3. Clasificador de Cliente")
    print("4. Salir")
    print("=" * 45)

    opcion = input("Selecciona una opcion (1-4): ")

    # --------------------------------------------------------
    # VALIDACION DE OPCION DEL MENU
    # --------------------------------------------------------
    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
        print(">> Opcion invalida. Intenta de nuevo.")
        continue

    # --------------------------------------------------------
    # OPCION 4: SALIR
    # --------------------------------------------------------
    if opcion == "4":
        print("\nCerrando el sistema... !Gracias por su visita!")
        break

    # ==========================================================
    # OPCION 1: VENTA DE COMBUSTIBLE
    # ==========================================================
    if opcion == "1":
        print("\n--- VENTA DE COMBUSTIBLE ---")
        tipo_combustible = input("Tipo de combustible (Magna/Premium/Diesel): ")

        # Validacion del precio por litro (debe ser positivo)
        while True:
            precio_texto = input("Precio por litro ($): ")
            try:
                precio_litro = float(precio_texto)
            except ValueError:
                print(">> Error: ingresa un numero valido.")
                continue

            if precio_litro <= 0:
                print(">> Error: el precio debe ser positivo.")
                continue
            break

        # Validacion de los litros cargados (debe ser positivo)
        while True:
            litros_texto = input("Cantidad de litros: ")
            try:
                litros = float(litros_texto)
            except ValueError:
                print(">> Error: ingresa un numero valido.")
                continue

            if litros <= 0:
                print(">> Error: la cantidad de litros debe ser positiva.")
                continue
            break

        total_venta = precio_litro * litros

        print("\n----- TICKET DE VENTA -----")
        print(f"{'Combustible:':<18}{tipo_combustible:>15}")
        print(f"{'Precio/litro:':<18}{'$' + format(precio_litro, '.2f'):>15}")
        print(f"{'Litros:':<18}{litros:>15.2f}")
        print("-" * 33)
        print(f"{'TOTAL A PAGAR:':<18}{'$' + format(total_venta, '.2f'):>15}")
        print("-" * 33)

    # ==========================================================
    # OPCION 2: SIMULACION DE RENDIMIENTO
    # ==========================================================
    elif opcion == "2":
        print("\n--- SIMULACION DE RENDIMIENTO ---")

        while True:
            km_texto = input("Kilometraje inicial del vehiculo (km): ")
            try:
                km_inicial = float(km_texto)
            except ValueError:
                print(">> Error: ingresa un numero valido.")
                continue
            if km_inicial < 0:
                print(">> Error: el kilometraje no puede ser negativo.")
                continue
            break

        while True:
            rendimiento_texto = input("Rendimiento del vehiculo (km por litro): ")
            try:
                rendimiento = float(rendimiento_texto)
            except ValueError:
                print(">> Error: ingresa un numero valido.")
                continue
            if rendimiento <= 0:
                print(">> Error: el rendimiento debe ser positivo.")
                continue
            break

        while True:
            meses_texto = input("Numero de meses a proyectar: ")
            if not meses_texto.isdigit() or int(meses_texto) <= 0:
                print(">> Error: ingresa un entero positivo.")
                continue
            meses = int(meses_texto)
            break

        while True:
            km_mensuales_texto = input("Km recorridos estimados por mes: ")
            try:
                km_mensuales = float(km_mensuales_texto)
            except ValueError:
                print(">> Error: ingresa un numero valido.")
                continue
            if km_mensuales <= 0:
                print(">> Error: los km mensuales deben ser positivos.")
                continue
            break

        # Factor de incremento de consumo (desgaste del motor), usado con potencia (**)
        factor_desgaste = 1.01

        print("\n----- PROYECCION DE RENDIMIENTO -----")
        print(f"{'Mes':<6}{'Km acumulados':>16}{'Litros consumidos':>20}{'Tanques completos':>20}{'Litros restantes':>18}")
        print("-" * 80)

        km_acumulado = km_inicial

        for mes in range(1, meses + 1):
            km_acumulado = km_acumulado + km_mensuales

            # Ajuste del rendimiento real segun el desgaste acumulado del motor (uso de **)
            rendimiento_ajustado = rendimiento / (factor_desgaste ** mes)

            litros_consumidos = km_mensuales / rendimiento_ajustado

            # Uso obligatorio de division entera (//) y residuo (%)
            tanques_completos = int(litros_consumidos) // 40
            litros_restantes = int(litros_consumidos) % 40

            print(f"{mes:<6}{km_acumulado:>16.1f}{litros_consumidos:>20.2f}{tanques_completos:>20}{litros_restantes:>18}")

        print("-" * 80)
        print("(Se asume un tanque estandar de 40 litros para el calculo de tanques completos)")

    # ==========================================================
    # OPCION 3: CLASIFICADOR DE CLIENTE
    # ==========================================================
    elif opcion == "3":
        print("\n--- CLASIFICADOR DE CLIENTE ---")

        while True:
            volumen_texto = input("Volumen de compra mensual del cliente (litros): ")
            try:
                volumen_mensual = float(volumen_texto)
            except ValueError:
                print(">> Error: ingresa un numero valido.")
                continue
            if volumen_mensual < 0:
                print(">> Error: el volumen no puede ser negativo.")
                continue
            break

        if volumen_mensual < 100:
            categoria = "Regular"
            descuento = 0
        elif volumen_mensual >= 100 and volumen_mensual <= 500:
            categoria = "Premium"
            descuento = 5
        else:
            categoria = "Flotilla"
            descuento = 12

        print("\n----- RESULTADO DE CLASIFICACION -----")
        print(f"{'Volumen mensual:':<20}{volumen_mensual:>10.2f} L")
        print(f"{'Categoria:':<20}{categoria:>10}")
        print(f"{'Descuento asignado:':<20}{descuento:>9}%")
