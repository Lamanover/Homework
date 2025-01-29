def custom_write(file_name, strings):
    strings_pos = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            byte_pos = file.tell()
            file.write(string + '\n')
            strings_pos[(index, byte_pos)] = string

    return strings_pos



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
