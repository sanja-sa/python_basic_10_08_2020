"""
Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. 
Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def validator_is_positive(val):
    return val > 0

def validator_is_nagative(val):
    return val < 0

# Схема приема данных от пользователя ( кортеж, т.к. схема практически меняеться редко )
sheme_model=(
    ("Положительное действительное число", float, (validator_is_positive, "быть положительным")),
    ("Отрицательное целое число", int, (validator_is_nagative, "быть отрицательным")),
    )

def input_data(param_name, param_type, validator):
    """Получаем данные от пользователя
    :param param_name: Текстовое обозначение параметра
    :param param_type: Тип параметра
    :param validator: Проверка параметра на доп условия
    :return: Результат принятого параметра
    """
    while True:
        try:
            param = param_type(input(f'Введите "{param_name}": '))
        except:
            print(f'"{param_name}" должно быть как {param_type}')
            continue

        if validator != None and not validator[0](param):
            print(f'Значение должно {validator[1]}')
            continue
        break
    return param

def my_func_1(x, y):
    """Возведение в степень методом **
    :param x: Число возводимое в степень
    :param y: Показатель степени
    :return: Число x в степени y
    """
    return x**y

def my_func_2(x, y):
    """Возведение в степень методом цикла
    :param x: Число возводимое в степень
    :param y: Показатель степени
    :return: Число x в степени y
    """
    x = 1/x if y < 0 else x
    result, cnt = 1, abs(y)
    if cnt == 0:
        return result
    while cnt:
        result *= x
        cnt -= 1
    return result

while True:
    continue_answ = input("Хотите вычислить степень чисела? ( Да ): ")
    if continue_answ.lower() != "да":
        break

    digits=[]
    for item in sheme_model:
        digits.append(input_data(item[0], item[1], item[2]))
    
    # TODO: Ошибка деления не 0 обработка
    print(my_func_1(digits[0], digits[1]))
    print(my_func_2(digits[0], digits[1]))