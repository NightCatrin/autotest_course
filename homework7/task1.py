# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False
import math


class Segment:

    def __init__(self, tuple1: tuple, tuple2: tuple):
        self.tuple1 = tuple1
        self.tuple2 = tuple2
        self.len = 0

    def length(self):
        """Метод возвращает длину отрезка с округлением до 2х знаков"""

        self.len = math.sqrt((self.tuple1[0] - self.tuple2[0]) ** 2 + (self.tuple1[1] - self.tuple2[1]) ** 2)

        return round(self.len, 2)

    def x_axis_intersection(self):
        """Метод проверяет пересечение оси абсцисс.
        Если y1*y2 < 0, то True"""

        if self.tuple1[1] * self.tuple2[1] < 0:
            return True
        else:
            return False

    def y_axis_intersection(self):
        """Метод проверяет пересечение оси ординат
        Если x1*x2 < 0, то True"""

        if self.tuple1[0] * self.tuple2[0] < 0:
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]

test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
