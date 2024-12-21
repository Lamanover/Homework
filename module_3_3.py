def print_params(a = 1, b = 'Cтрока', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [12, 'Hello', False]
values_dict = {'a' : 4, 'b' : 10, 'c' : 15}

print_params(*values_list)
print_params(**values_dict)

values_list_2 =[52.13, 'Стобец']

print_params(*values_list_2, 55)