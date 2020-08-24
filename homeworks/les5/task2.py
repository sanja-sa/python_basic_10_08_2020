"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""


import os

try:
    with open(os.path.join(os.path.dirname(__file__), "task1.py"), "r", encoding='UTF-8') as file:
        cnt_lines = 0
        while True:
            content = file.readline()
            if not content:
                break
            cnt_lines += 1
            print(f'{cnt_lines}. {content[:-1]}  ({len(content.split())})')
            
except IOError as e:
    print(f'Произошла ошибка ввода-вывода: {e}')