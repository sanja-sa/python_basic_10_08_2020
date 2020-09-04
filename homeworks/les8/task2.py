"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ValidatorValuesException(Exception):
    """
    Класс собственного исключения
    """
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        digit1, digit2 = input("Введите два числа для деления: ").split()
    except ValueError:
        print("Заканчиваем работу с программой")
        break
    try:
        digit1, digit2 = float(digit1), float(digit2)
        if not digit2:
            raise ValidatorValuesException("Ошибка деоения на ноль")
        print(f'{digit1/digit2}')
    except ValidatorValuesException as err:
        print(err)
    except:
        print("Введите пожалуйста цифры")