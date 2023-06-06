# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt

# Здесь пишем код
#

new_string = []

with open('test_file/task1_data.txt', mode='r',  encoding='utf-8') as data_file:
    for one_line in data_file.readlines():
        new_string.append(''.join([char for char in one_line if not char.isdigit]))

with open('test_file/task1_answer.txt', 'a', encoding='utf-8') as answer_file:
    answer_file.writelines(new_string)


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
