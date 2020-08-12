"""
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict.
"""


list_months = ['зима','весна','лето','осень']
dict_months = {0:'зима',1:'весна',2:'лето',3:'осень'}

entered_month = 0
not_correct = True

while not_correct:
    try:
        entered_month = int(input("Please enter number of month ( 1-12 ): "))
        if entered_month >= 1 and entered_month <= 12:
            not_correct = False
    except:
        print("Please enter only digits")

month = entered_month%12
print(f'This month is from list "{list_months[month//3]}"')
print(f'This month is from dict "{dict_months[month//3]}"')