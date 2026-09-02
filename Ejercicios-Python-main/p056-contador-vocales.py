# 🔤 Cuenta vocales, consonantes y otros caracteres de una frase.


def analizar_frase(frase):
    vocales_validas = "aeiouáéíóúü"
    vocales = 0
    consonantes = 0
    otros = 0
    indice = 0

    while indice < len(frase):
        caracter = frase[indice].lower()
        if caracter.isalpha():
            if caracter in vocales_validas:
                vocales += 1
            else:
                consonantes += 1
        else:
            otros += 1
        indice += 1

    return vocales, consonantes, otros


def main():
    while True:
        frase = input("\nIntroduce una frase: ")
        vocales, consonantes, otros = analizar_frase(frase)

        print("\n📊 Analisis de la frase:")
        print(f"🔴 Numero de vocales: {vocales}")
        print(f"🔵 Numero de consonantes: {consonantes}")
        print(f"⚪ Numero de caracteres no alfabeticos: {otros}")

        if input("\nDeseas analizar otra frase (S/N)? ").strip().upper() == "N":
            break

    print("\n✅ Fin del programa. Gracias.")


if __name__ == "__main__":
    main()
