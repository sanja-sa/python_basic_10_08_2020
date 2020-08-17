"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и 
после этого завершить программу.
"""


def my_summ(digit_container) -> tuple:
    """Суммируем элементы контейнера
    :param digit_container: Контейнер для суммирования
    :return: (Сумма всех элементов, Символ конца ввода)
    """
    idx = 0
    result = 0
    try:
        while True: 
            result += float(digit_container[idx])
            idx += 1
    except ValueError:
        return (result, digit_container[idx])
    except IndexError:
        return (result, None)

result_summ= 0
while True:
    input_list = input("Введите серию чисел, разделенных пробелом ( для выхода введите 'e' ): ").split()
    all_summ, escape_str = my_summ(input_list)
    result_summ += all_summ
    print(f'Текущее результирующее значение сумм: {result_summ}')
    if escape_str == 'e':
        print("Расчет закончен")
        break


    


