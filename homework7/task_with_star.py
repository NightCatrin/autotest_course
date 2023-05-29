# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

# Здесь пишем код
class RomanNums:
    def __init__(self, roman_num):
        self.roman_num = roman_num
        self.conversion_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                                'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                                'X': 10, 'IX': 9, 'V': 5, 'IV': 4,
                                'I': 1}

    def from_roman(self):
        """Метод переводит римскую запись числа в арабскую
        arab_num: Арабское число
        num: Число для проверки последовательности римских цифр"""

        arab_num = 0
        num = 0

        for roman_value in self.roman_num[::-1]:
            value = self.conversion_dict[roman_value]

            if value >= num:
                arab_num += value
                num = value
            else:
                arab_num -= value

        return arab_num

    def is_palindrome(self):
        """Метод определяет, является ли арабское число палиндромом
        reversed_num: перевернутое римское число в виде строки"""

        reversed_num = ''.join(reversed(str(self.from_roman())))

        if str(self.from_roman()) == reversed_num:
            return True
        else:
            return False


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]

test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')
