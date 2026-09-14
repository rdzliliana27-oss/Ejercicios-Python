# 🎨 Combina colores de texto y fondo usando ciclos for anidados.

import sys


sys.stdout.reconfigure(encoding="utf-8")


COLORES = {
    "negro": 30,
    "rojo": 31,
    "verde": 32,
    "amarillo": 33,
    "azul": 34,
    "magenta": 35,
    "cian": 36,
    "blanco": 37,
}


def main():
    print("🎨 Combinaciones de colores ANSI\n")
    nombres = list(COLORES)

    for posicion, nombre_texto in enumerate(nombres, start=1):
        print(f"{posicion}. {nombre_texto}")

    while True:
        try:
            cantidad = int(input("\n🌈 ¿Cuántos colores deseas combinar? "))
            if cantidad < 1 or cantidad > len(nombres):
                raise ValueError
            break
        except ValueError:
            print(f"⚠️ Elige un número entre 1 y {len(nombres)}.")

    seleccion = nombres[:cantidad]
    print("\n✨ Combinaciones (texto sobre fondo):")
    for nombre_texto in seleccion:
        for nombre_fondo in seleccion:
            codigo_texto = COLORES[nombre_texto]
            codigo_fondo = COLORES[nombre_fondo] + 10
            muestra = f"\033[{codigo_texto};{codigo_fondo}m {nombre_texto} / {nombre_fondo} \033[0m"
            print(muestra)


if __name__ == "__main__":
    main()
