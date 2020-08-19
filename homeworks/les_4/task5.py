"""
Реализовать формирование списка, используя функцию range() и возможности генератора. 
В список должны войти четные числа от 100 до 1000 (включая границы). 
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


from functools import reduce


def my_reduce(func, container):
    """
    Функция формирующая продукт двух значений в списке через func
    :param func: Функция расчета двух значений в зависимости от предыдущего
    :param container: Контейнер вычисления
    :return: Рассчитанное значение по всем элементам
    """
    idx = 1
    try:
        result = container[0]
    except IndexError:
        raise TypeError
    try:
        while True:
            result = func(result, container[idx])
            idx += 1
    except IndexError:
        pass
    return result

print(my_reduce(lambda x,y: x*y, [digit for digit in range(100, 1001) if not digit&1]))
print(reduce(lambda x,y: x*y, [digit for digit in range(100, 1001) if not digit&1]))
