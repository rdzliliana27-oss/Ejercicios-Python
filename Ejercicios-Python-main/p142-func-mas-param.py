# p142-func-mas-param.py


def saludatodos(*todos: str) -> None:
    for nombre in todos:
        print(f"Saludos a {nombre}")


saludatodos("Juan", "Pedro", "Luis")
