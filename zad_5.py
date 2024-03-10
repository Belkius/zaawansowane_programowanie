def check_list(value_list: list, number: int) -> bool:
    if number in value_list:
        return True
    else:
        return False


number_in_list = check_list([1, 2, 3, 4], 1)
print(number_in_list)
