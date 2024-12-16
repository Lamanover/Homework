n = int(input('Введите число от 3 до 20: '))
result = []
for number_1 in range(1, n):
    for number_2 in range(1, n):
        c = number_1 + number_2
        for i in range(1, n):
            if n % c == 0:
                if number_1 >= number_2:
                    continue
                else:
                    result.append(number_1)
                    result.append(number_2)
            break

print(result)






