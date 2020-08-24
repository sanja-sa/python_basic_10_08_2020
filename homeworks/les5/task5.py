"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


import random, os

file_name = os.path.join(os.path.dirname(__file__), "task5_result.txt")

def gener_rand_ints_file(file_path:str):
    """
    Генерация файла с числами в одну строку, разделенные пробелами
    :param file_path: Путь до файла
    """
    with open(file_path, "w", encoding='UTF-8') as file:
        cnt_digits = 1000
        while cnt_digits:
            file.write(f'{random.randrange(5,10000)} ')
            cnt_digits -= 1


def calc_summ(file_path:str) -> float:
    """
    Подсчет суммы чисел в файле
    :param file_path: Путь до файла
    :return: Сумма чисел
    """
    result = 0
    with open(file_path, "r", encoding='UTF-8') as file:
        digits_list = file.readline().split()
        for itm in digits_list:
            result += float(itm)
    return result

try:
    gener_rand_ints_file(file_name)
    print(calc_summ(file_name))
except IOError as e:
    print(f'Произошла ошибка ввода-вывода файла: {e}')
except:
    print(f'Произошла ошибка в структуре файла')