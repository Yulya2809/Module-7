def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    number_str = 0
    bait_nach = file.seek(0)
    for i in strings:
        file.write(i+'\n')
        number_str += 1
        key = (number_str, bait_nach)
        string_positions[key] = i
        bait_nach = file.tell()
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
