"""
Создать программно файл в текстовом формате, 
записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""


while True:
    input_value = input("Введите данные для записи в файл (Для выхода введите 'exit'): ")

    if input_value == "exit":
        break

    try:
        with open("user_input_data.txt", "a", encoding='UTF-8') as file:
            file.write(input_value+"\n")
    except IOError:
        print("Произошла ошибка ввода-вывода!")
