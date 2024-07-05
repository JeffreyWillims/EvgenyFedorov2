def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

values_list = [7, 'String', True]
values_dict = {'a': 125, 'b': 'Line', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "'Cтрока'"]
print_params(*values_list_2, 42)