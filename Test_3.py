data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    total_sum = 0
    for i in args:
        if isinstance(i, (int, float)):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            total_sum += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for key, value in i.items():
                total_sum += len(key)
                total_sum += calculate_structure_sum(value)
    return total_sum

result = calculate_structure_sum(data_structure)
print(result)