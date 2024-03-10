def merge_lists(list_1: list, list_2: list) -> list:
    merged_set = set(list_1 + list_2)
    merged_list = list(merged_set)
    return[number ** 3 for number in merged_set]


list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
merged_lists = merge_lists(list_1, list_2)
print(merged_lists)
