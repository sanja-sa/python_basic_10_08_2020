"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове
"""


entered_words = []
while len(entered_words)<2:
    entered_words = input("Please enter some words splitted by ' ': ").split()

for idx,itm in enumerate(entered_words):
    print(f'{idx+1}. {itm[:10]+"..." if len(itm) > 10 else itm}')
    