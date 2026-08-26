#Ejericio de verifica suma
# ejercicio que solicita al usuario tres números enteros y verifica si la suma de dos de ellos es igual al tercero.

def main():
    print("🧮 --- Verificar si la suma de dos números es igual a un tercero ---")
    n1, n2, n3 = map(int, input("Dame 3 números enteros separados por espacio: ").split())

    if n1 + n2 == n3:
        print(f"✅ n1 + n2 es igual a n3 ({n1} + {n2} = {n3})")
    elif n1 + n3 == n2:
        print(f"✅ n1 + n3 es igual a n2 ({n1} + {n3} = {n2})")
    elif n2 + n3 == n1:
        print(f"✅ n2 + n3 es igual a n1 ({n2} + {n3} = {n1})")
    else:
        print("❌ Ninguna combinación de suma es igual al tercer número.")


if __name__ == "__main__":
    main()