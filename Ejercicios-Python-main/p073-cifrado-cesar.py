# 🔐 Cifra un mensaje usando el cifrado Cesar.


def cifrar(mensaje, desplazamiento):
    resultado = ""
    for caracter in mensaje:
        if "a" <= caracter <= "z":
            base = ord("a")
        elif "A" <= caracter <= "Z":
            base = ord("A")
        else:
            resultado += caracter
            continue

        codigo = base + (ord(caracter) - base + desplazamiento) % 26
        resultado += chr(codigo)
    return resultado


def main():
    continuar = "S"
    while continuar == "S":
        mensaje = input("💬 Ingresa el mensaje a cifrar: ")
        while True:
            try:
                desplazamiento = int(input("🔑 Ingresa el desplazamiento: "))
                break
            except ValueError:
                print("⚠️ Error: introduce un entero.")

        print(f"📨 Mensaje original: {mensaje}")
        print(f"🔒 Mensaje cifrado: {cifrar(mensaje, desplazamiento)}")
        continuar = input("🔁 Desea cifrar otro mensaje (S/N)? ").strip().upper()


if __name__ == "__main__":
    main()
