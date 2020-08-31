"""
Реализовать класс Matrix (матрица). 
Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки 
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    """
    Класс отвечающий за работу с матрицами
    """


    def __init__(self, elems:list):
        """
        Конструктор класса матрицы
        :param elems: Список элементов (строки, столбцы)
        """
        # Элементы матрицы row position
        self.__elems = elems
        # Перерасчитать максимальный размер цифры в строке ( используется для вывода на экран )
        self.__max_len_digit_recalc = True
        # Текущий максимальный размер цифры в строке ( используется для вывода на экран )
        self.__max_len_digit = 1


    def __calc_max_cnt_in_digit(self):
        """
        Максимальную цифру в матрице, для выравнивания вывода
        """
        max_len_digit = 1
        for itm in self.__elems:
            for i in itm:
                digit_len = len(str(i))
                max_len_digit = max_len_digit if digit_len < max_len_digit else digit_len
        self.__max_len_digit_recalc = False
        return max_len_digit


    def __str__(self):
        self.__max_len_digit = self.__calc_max_cnt_in_digit() if self.__max_len_digit_recalc else self.__max_len_digit
        str_out = ""
        curr_row = 0
        cnt_rows = len(self.__elems)
        cnt_cols = len(self.__elems[0])
        while curr_row != cnt_rows:
            curr_col = 0
            str_out += "|"
            while curr_col != cnt_cols:
                str_out += f'{self.__elems[curr_row][curr_col]:>{self.__max_len_digit}}' + ("|\n" if curr_col + 1 == cnt_cols else " ")
                curr_col += 1
            curr_row += 1
        return str_out[:-1]

    def __add__(self, other:"Matrix")->"Matrix":
        self.__max_len_digit_recalc = True
        return Matrix(list([list(map(sum, zip(self.__elems[idx],other.__elems[idx]))) for idx,_ in enumerate(self.__elems)]))

m1 = Matrix([[32211,22],[37,143],[51,86]])
print(m1)
print("")
m2 = Matrix([[1,2,3],[4,5,6],[7,8, 9]])
print(m2)
print("")
m3 = Matrix([[3,5,8,3],[8,3,7,1]])
print(m3)
m4 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
print(m3)
print("")
m5=m2+m4
print(m5)