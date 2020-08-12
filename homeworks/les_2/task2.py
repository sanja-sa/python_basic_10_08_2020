"""
Для списка реализовать обмен значений соседних элементов, т.е. 
значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""


input_list = input("Please enter some texts splits by ','").split(",")

print(f'You have entered list: {input_list}')
for idx in range(0,len(input_list)-1,2):
   input_list[idx],input_list[idx+1] = input_list[idx+1],input_list[idx]     
print(f'Result list: {input_list}')

