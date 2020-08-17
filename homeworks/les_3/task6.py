"""
Реализовать функцию int_func(), 
принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. 
В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(text:str) -> str:
    if len(text) == 0:
        return ""
    return text[0].upper() + text[1:]

def func_list(container) -> bool:
    idx = 0
    try:
        while True:
            if not container[idx].islower() or not container[idx].isalpha() or not container[idx].isascii():
                return False
            container[idx] = int_func(container[idx])
            idx += 1            
    except:
        return True
    return True

while True:
    input_list = input("Введите серию символов латинмкого алфавита, разделенных пробелом: ").split()
    
    if not func_list(input_list):
        print("Только латинские символы нижнего регистра")
        continue
    out = ""
    for itm in input_list: out += f"{itm} "
    print(out)
    break
