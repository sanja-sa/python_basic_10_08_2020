"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""


import os, json

cnt_strings = 1
firm_list = []
try:
    with open(os.path.join(os.path.dirname(__file__), "task7.txt"), "r", encoding='UTF-8') as file:
        while True:
            content = file.readline()
            if not content:
                break

            # Получение данных фирмы
            firm_data  = content.split()
            if len(firm_data) != 4:
                print(f'Структура файла нарушена в строке: {cnt_strings}')
                exit()

            # Проверка типов данных
            firm_data[2] = float(firm_data[2])
            firm_data[3] = float(firm_data[3].strip('.'))

            # Добавление прибыли
            firm_data.append(firm_data[2] - firm_data[3])

            # Добавление в общий список
            firm_list.append(firm_data)
            cnt_strings += 1

except IOError as e:
    print(f'Произошла ошибка ввода-вывода файла: {e}')
except:
    print(f'Произошла ошибка в структуре данных файла')

def is_positive_profit(firm_data:list):
    """
    Функтор фильтрации по положительной выручке
    :param firm_data: Данные фирмы
    :param top: Верхняя граница
    :param bottom: Нижняя граница
    """
    return  firm_data[4] > 0

def filter_firm(filter_func, filter_dict:dict, firms_list:list):
    """
    Фильтрация фирм по функтору
    :param filter_func: Функтор фильтрации
    :param filter_dict: Параметры фильтрации
    :param firms_list: Список фирм
    """
    idx = 0
    cnt = len(firms_list)
    while cnt:
        if filter_func(firms_list[idx], **filter_dict):
            yield firms_list[idx]
        cnt -=1
        idx += 1

def get_positive_average_report(firms_list:list):
    """
    Генерация отчета по положительной средней выручке
    :param firms_list: Список фирм
    """
    good_firms_dict = {}
    cnt_firms = 0
    average_profit = 0
    for itm in filter_firm(is_positive_profit, {}, firm_list):
        good_firms_dict[itm[0]] = itm[4]
        average_profit += itm[4]
        cnt_firms += 1
    return [good_firms_dict, {"average_profit":average_profit/cnt_firms}]

result_list = get_positive_average_report(firm_list)

# Сохранение в json
with open(os.path.join(os.path.dirname(__file__), "task7_result.json"), "w", encoding='UTF-8') as write_f:
    json.dump(result_list, write_f)
