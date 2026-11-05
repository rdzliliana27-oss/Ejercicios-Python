# p145-cuadro-caracter.py
# Dados renglones, columnas y carácter, dibuja un cuadro


def dibuja_cuadro(renglones: int, columnas: int, caracter: str) -> None:
    for _ in range(renglones):
        for _ in range(columnas):
            print(caracter, end="")
        print("")


renglones = int(input("Ingrese el número de renglones del cuadro: "))
columnas = int(input("Ingrese el número de columnas del cuadro: "))
caracter = input("Ingrese el carácter para dibujar el cuadro: ")
dibuja_cuadro(renglones, columnas, caracter)
