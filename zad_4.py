def two_greater(num1: int, num2: int, num3: int) -> bool:
    if num1 + num2 > num3:
        return True
    else:
        return False


two_are_grater = two_greater(5, 2, 4)
print(two_are_grater)
