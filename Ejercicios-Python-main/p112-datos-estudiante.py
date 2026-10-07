print("Registro de datos del estudiante")

nombre = input("Nombre: ").strip()
matricula = input("Matricula: ").strip()
carrera = input("Carrera: ").strip()

try:
    edad = int(input("Edad: "))
except ValueError:
    print("Error: la edad debe ser un numero entero.")
else:
    if not nombre or not matricula or not carrera:
        print("Error: todos los campos de texto son obligatorios.")
    elif edad < 0:
        print("Error: la edad no puede ser negativa.")
    else:
        estudiante = {
            "nombre": nombre,
            "matricula": matricula,
            "carrera": carrera,
            "edad": edad,
        }

        print("\nDatos registrados:")
        for campo, valor in estudiante.items():
            print(f"{campo.title()}: {valor}")