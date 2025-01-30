team1_num = input('Введите количество участников первой команды: ')
team2_num = input('Введите количество участников второй команды: ')

score_1 = input('Введите количество решенных задач первой командой: ')
score_2 = input('Введите количество решенных задач второй командой: ')

team_1_time = input('Введите время затраченное на решение задач первой командой в секундах: ')
team_2_time = input('Введите время затраченное на решение задач второй командой в секундах: ')

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team_1_time > team_2_time:
        return 'Победила команда Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team_1_time < team_2_time:
        return 'Победила команда Волшебники данных!'
    else:
        return 'Ничья!'

tasks_total = int(score_1) + int(score_2)
time_avg = ((float(team_1_time) / int(score_1)) + float(team_2_time) / int(score_2)) / 2

print('В первой команде Мастера кода %s участников!' %team1_num)
print('Во второй команде Волшебники данных %s участников!' %team2_num)
print('Команда Мастера кода решили: {}!'.format(score_1))
print('Команда Волшебники данных решили: {}!'.format(score_2))
print('Команда Мастера кода решили задачи за {} с!'.format(team_1_time))
print('Команда Волшебники данных решили задачи за {} с!'.format(team_2_time))
print(f'Количество решенных задач по командам: {score_1}, {score_2}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунд на задачу!')
print(f'Результаты биты: {challenge_result()}')




