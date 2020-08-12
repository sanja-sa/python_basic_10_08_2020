"""
Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""


items_types = (str,str,list,list,float,float,int)
items_params = ["Russia",["St.Peterburg","Moskow","Ekaterinburg"],[100,200,300],123.3,(1,"Curred")]

items_params.append(101)
items_params.insert(0,"France")

# TODO: Add check for equal length 'items_types' and 'items_params'
# TODO: Set types in 'items_params'

try:
    for idx,item in enumerate(items_params):
        if items_types[idx] is not type(item):
            err = f'Exception: Item "{item}" type "{type(item)}" not "{items_types[idx]}"'
            raise TypeError(err)
        else:
            print(f'Item {item} has correct type - {type(item)}')
except TypeError as err:
    print(err)
