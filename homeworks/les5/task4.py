"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""


import os

counter_dict = {"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}
split_symbol = " — "

cnt_strings = 1
try:
    with open(os.path.join(os.path.dirname(__file__), "task4.txt"), "r", encoding='UTF-8') as file:
        while True:
            content = file.readline()
            if not content:
                break

            # Получение списка строки числительных
            count_data = content.split(split_symbol)
            if len(count_data) != 2:
                print(f'Структура файла числительных нарушена в строке: {cnt_strings}')
                exit()

            cnt_strings += 1

            with open(os.path.join(os.path.dirname(__file__), "task4_result.txt"), "a", encoding='UTF-8') as result_file:
                result_file.write(f'{counter_dict[count_data[0]]}{split_symbol}{count_data[1]}')
            
except IOError as e:
    print(f'Произошла ошибка ввода-вывода файла: {e}')
