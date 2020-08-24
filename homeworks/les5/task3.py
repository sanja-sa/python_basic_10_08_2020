"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.

Файл будет в виде: 

Иванов А.П,10000
Сидоров П.В.,15000
Федоров З.Г.,30000
...
"""

import os

def is_salary_in_border(employeer_data:list, top:float=0, bottom:float=0):
    """
    Функтор фильтрации по зарплате
    :param employeer_data: Данные пользователя
    :param top: Верхняя граница зарплаты
    :param bottom: Нижняя граница зарплаты
    """
    return employeer_data[1] >= bottom and employeer_data[1] <= top

def filter_employeers(filter_func, filter_dict:dict, employeer_list:list):
    """
    Фильтрация сотрудников по функтору
    :param filter_func: Функтор фильтрации
    :param filter_dict: Параметры фильтрации
    :param employeer_list: Список сотрудников
    """
    idx = 0
    cnt = len(employeer_list)
    while cnt:
        if filter_func(employeer_list[idx], **filter_dict):
            yield employeer_list[idx]
        cnt -=1
        idx += 1

def sum(employeer_data:list, result:float)->float:
    """
    Функтор суммиирования к результату
    :param employeer_data: Данные пользователя
    :param result: Предыдущий результат

    """
    return (result + employeer_data[1])

def visitor_employeers(visitor_func, visitor_initializer, employeers_list:list):
    """
    Посетитель сотрудников
    :param employees_list: Список сотрудников с tuple их зарплатами
    :param visitor_func: Функтор посетителя
    :param visitor_initializer: Первоначальная инициализация для результата
    :return: Результат работы последовательного алгоритма visitor_func
    """
    idx = 0
    cnt = len(employeers_list)
    result = visitor_initializer
    while cnt:
        result = visitor_func(employeers_list[idx], result)
        cnt -=1
        idx += 1
    return result

empl_list = []
try:
    with open(os.path.join(os.path.dirname(__file__), "task3.txt"), "r", encoding='UTF-8') as file:
        while True:
            content = file.readline()
            if not content:
                break

            # Получение списка чтроки данных сотрудника
            employeer_data = content.split(",")
            if len(employeer_data) != 2:
                print(f'Структура файла сотрудников нарушена в строке: {len(empl_list)+1}')
                exit()

            # Чистим от нежелательных символов
            employeer_data[0] = employeer_data[0].strip()

            try:
                employeer_data[1] = float(employeer_data[1].strip("\n"))
            except ValueError:
                print(f'Тип данных зарплаты сотрудников нарушен в строке: {len(empl_list)+1}')
                exit()

            empl_list.append(employeer_data)
            
except IOError as e:
    print(f'Произошла ошибка ввода-вывода файла: {e}')

# Распечатаем имена сотрудников с зарплатой менее 20000
for idx,itm in enumerate(filter_employeers(is_salary_in_border, {"top":20000}, empl_list)):
    print(f'{idx+1}. {itm[0]}')

print(f'Средняя зарплата сотрудников: {visitor_employeers(sum, 0, empl_list)/len(empl_list):.2f}')