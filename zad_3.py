def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


even_result = is_even(4)
if even_result:
    print("Liczba parzysta!")
else:
    print("Liczba nieparzysta!")
    