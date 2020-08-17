"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def digit_input(ask_text):
    """Получаем число от пользователя
    :param ask_text: Текстовое обозначение числа
    :return: Результат принятого числа
    """
    while True:
        try:
            digit = float(input(f'Введите "{ask_text}": '))
        except:
            print(f'"{ask_text}" должно быть числом')
            continue
        break
    return digit

def divide(devidend, devider):
    """Вычисляет деление двух чисел
    :param numerator: Делимое
    :param numerator: Делитель
    :return: Результат деления
    """
    # TODO: Ексепшн ZeroDivisionError можно перенести сюда, но не факт, что будет лучше
    return devidend/devider


while True:
    continue_answ = input("Хотите вычислить деление 2 чисел? ( Да ): ")
    if continue_answ.lower() != "да":
        break

    devidend = digit_input("Делимое")
    devider = digit_input("Делитель")

    try:
        print(divide(float(devidend),float(devider)))
    except ZeroDivisionError:
        print("Ошибка деления на ноль.")
