# Напишите класс Trigon, для инициализации передаётся неизвестное кол-во атрибутов
# В классе при инициализации происходит проверка на корректность переданных данных и генерируются следующие исключения:
# 1) Если хотя бы одна сторона передана не числом,
# то падаем с TypeError и текстом 'Стороны должны быть числами'
# 2) Если хотя бы одна сторона передана нулем или отрицательным числом,
# то падаем с ValueError и текстом 'Стороны должны быть положительными'
# 3) Если не соблюдается неравество треугольника,
# то Exception и текст "Не треугольник"
# 4) Если передано не 3 аргумента, то IndexError "Передано {n} аргументов, а ожидается 3", где n - кол-во аргументов

import unittest  # Не удалять


# Здесь пишем код
class Trigon:
    def __init__(self, *args):
        try:
            num_a = args[0]
            num_b = args[1]
            num_c = args[2]
            sum_num = num_a + num_b + num_c
            if num_a < 0 or num_b < 0 or num_c < 0:
                raise ValueError('Стороны должны быть положительными')
        except TypeError:
            raise TypeError('Стороны должны быть числами')
        except IndexError:
            if len(args) != 3:
                raise IndexError(f'Передано {len(args)} аргументов, а ожидается 3')
            raise IndexError(f'Передано {len(args)} аргументов, а ожидается 3')

        if not(num_a + num_b > num_c and num_b + num_c > num_a and num_a + num_c > num_b):
            raise Exception('Не треугольник')


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
class MyTestCase(unittest.TestCase):

    def test(self):
        data = [(3, '7', 5), (-3, 7, 5), (2, 5, 2), (3, 4, 5, 6), (3, 4), (3, 4, 5)]

        test_data = [('Стороны должны быть числами', 'TypeError'),
                     ('Стороны должны быть положительными', 'ValueError'),
                     ("Не треугольник", 'Exception'),
                     ("Передано 4 аргументов, а ожидается 3", 'IndexError'),
                     ("Передано 2 аргументов, а ожидается 3", 'IndexError'),
                     0]
        for i, d in enumerate(data):
            try:
                Trigon(*data[i])
            except Exception as e:
                assert e.args[0] == test_data[i][0], 'Исключение имеет неправильный текст'
                assert type(e).__name__ == test_data[i][1], 'У исключения неправильный тип'

        print('Всё ок')


if __name__ == '__main__':
    unittest.main()