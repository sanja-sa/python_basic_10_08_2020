"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


import os

cnt_strings = 1
subject_dict = {}
try:
    with open(os.path.join(os.path.dirname(__file__), "task6.txt"), "r", encoding='UTF-8') as file:
        while True:
            content = file.readline()
            if not content:
                break

            # Получение списка предметов
            subject_data = content.split()
            if len(subject_data) != 4:
                print(f'Структура файла предметов нарушена в строке: {cnt_strings}')
                exit()

            # Чистим данные
            subject_data[0] = subject_data[0].strip(":")
            subject_data[1] = int(subject_data[1].strip("(л)").replace("—","0"))
            subject_data[2] = int(subject_data[2].strip("(пр)").replace("—","0"))
            subject_data[3] = int(subject_data[3].strip(".").strip("(лаб)").replace("—","0"))
            subject_dict[subject_data[0]] = sum(subject_data[1:])
            cnt_strings += 1

except IOError as e:
    print(f'Произошла ошибка ввода-вывода файла: {e}')
except:
    print(f'Произошла ошибка в структуре файла')

print(subject_dict)