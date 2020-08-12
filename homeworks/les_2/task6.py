"""
Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
(характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, 
в котором каждый ключ — характеристика товара, например название, 
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


sheme = (("название",str,"строка"), ("цена",int,"цифра"), ("количество",int,"цифра"), ("ед",str,"строка"))
items = []

qu = "Please enter item in format: \""
for itm in sheme:
    qu += str(itm[0]).upper() + f'({itm[2]}),'
qu = qu[:-1] + "\" (for exit enter 'exit'):\n"

while True:        
    item = input(qu).split(",")

    # Check len consistent
    if len(item) != len(sheme):
        if len(item) and item[0] == "exit":
            break
        print("Please enter items as in format!")
        continue

    # Check all types is consistent
    err= ""
    list_item={}
    for idx,itm in enumerate(sheme):
        if itm[1] is str:
            list_item[itm[0]]=item[idx]
        elif itm[1] is int:
            try:
                list_item[itm[0]]=int(item[idx])
            except:
                err=f'Please enter "{itm[0]}" as "{itm[2]}"!'   
                break
    if err:
        print(err)
        continue

    items.append((len(items)+1,list_item))

print(items)

# Create statistics
by_sheme_dict = {itm[0]:[itms[1][itm[0]] for itms in items] for itm in sheme}
print(by_sheme_dict)
