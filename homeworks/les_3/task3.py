"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
и возвращает сумму наибольших двух аргументов.
"""


def sort_less(arg_1, arg_2):
    """Функтор для функции сортировки по уменьшению 
    :return: True если меньший arg_1
    """
    return arg_1 > arg_2

def sort_more(arg_1, arg_2):
    """Функтор для функции сортировки по edtkbxtyb.
    :return: True если больший arg_1
    """
    return arg_1 < arg_2

def my_sorted(sort_func, sort_container):
    """Сортировка значения в контейнере вверх максимальные ( пузырек )
    :param func: Функция сортировки
    :param sort_container:  Контейнер, который сортируем
    :return: Отсортированный list
    """
    def up_max(from_idx, to_idx, container):
        idx = from_idx+1
        if idx == to_idx:
            return container[from_idx]
        while idx < to_idx:
            if sort_func(container[from_idx], container[idx]):
                container[from_idx], container[idx] = container[idx], container[from_idx]
            idx += 1
        return container[from_idx]

    idx = 0
    idx_max = len(sort_container)
    while idx < idx_max:
        yield up_max(idx, idx_max, sort_container)
        idx+=1
        
# Для теста
print(list(my_sorted(sort_less, [1, 51, -10, 21])))

def my_func(arg_1, arg_2, arg_3):
    """Возврат суммы двух максимальных аргументов
    :param arg_1: 1 Аргумент
    :param arg_2: 2 Аргумент
    :param arg_3: 3 Аргумент
    :return: Сумма
    """
    it = my_sorted(sort_more, [arg_1, arg_2, arg_3])
    return next(it) + next(it)

print(my_func(1,9,10))