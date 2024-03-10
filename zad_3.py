def are_even(numbers_list: list):
    even_nums = []
    for i in range(len(numbers_list)):
        if numbers_list[i] % 2 == 0:
            even_nums.append(numbers_list[i])
    print(f"Liczby parzyste{even_nums}")


numbers = [4, 1, 2, 3, 4, 5, 7, 8, 9, 3, 4, 5, 63, 2, 6, 0, 7]
are_even(numbers)
