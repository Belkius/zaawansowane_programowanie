def hello(name: str, surname: str) -> str:
    response = f"Cześć {name} {surname}!"
    return response


hello_greg = hello("Grzegorz", "Bel")
print(hello_greg)
