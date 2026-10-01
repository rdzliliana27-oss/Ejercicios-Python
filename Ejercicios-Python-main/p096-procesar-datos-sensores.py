import random

print("Simulacion y procesamiento de datos de dos sensores\n")

sensor_a_datos = []
sensor_b_datos = []

for _ in range(10):
    sensor_a_datos.append(random.randint(1, 100))
    sensor_b_datos.append(random.randint(1, 100))

print("--- Datos originales de los sensores ---")
print(f"Sensor A: {sensor_a_datos}")
print(f"Sensor B: {sensor_b_datos}")

sensor_a_transformados = []
sensor_b_transformados = []
datos_combinados = []

for posicion in range(10):
    dato_a = sensor_a_datos[posicion] ** 2
    dato_b = sensor_b_datos[posicion] ** 2
    sensor_a_transformados.append(dato_a)
    sensor_b_transformados.append(dato_b)
    datos_combinados.append(dato_a + dato_b)

print("\n--- Datos procesados ---")
print(f"Sensor A (al cuadrado): {sensor_a_transformados}")
print(f"Sensor B (al cuadrado): {sensor_b_transformados}")
print(f"Suma combinada: {datos_combinados}")