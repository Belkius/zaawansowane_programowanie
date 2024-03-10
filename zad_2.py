def double_values(value_list: list):
    for i in range(len(value_list)):
        value_list[i] *= 2
    print(value_list)


def double_values_short(value_list: list):
    print([number * 2 for number in value_list])


values_list = [4, 1, 2, 3, 4]
double_values(values_list)
values_list = [4, 1, 2, 3, 4]
double_values_short(values_list)
