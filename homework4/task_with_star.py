# Задача со ЗВЁЗДОЧКОЙ. Решать НЕ обязательно.
# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):

    array_num = [int(a) for a in str(num)]
    y = array_num.copy()
    index = 0
    new_array = []
    new_num = ''

    for i in range(len(array_num)):
        while array_num[i] < 10:
            num_sum = sum(array_num)
            if num_sum % 3 == 0:
                new_array.append(array_num.copy())
                array_num[index] += 1
            else:
                array_num[index] += 1
        array_num[index] = y[index]
        index += 1

    max_array = max(new_array)

    for i in max_array:
        new_num += str(i)

    return int(new_num)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')