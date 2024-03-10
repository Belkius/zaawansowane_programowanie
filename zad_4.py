def print_second(numbers_list: list):
    second = []
    for i in range(1, len(numbers_list), 2):
        second.append(numbers_list[i])
    print(f"Co druga liczba {second}")


numbers = [4, 1, 2, 3, 4, 5, 7, 8, 9, 3, 4, 5, 63, 2, 6, 0, 7]
print_second(numbers)
