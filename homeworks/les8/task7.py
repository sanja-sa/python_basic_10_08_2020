"""
Реализовать проект «Операции с комплексными числами». 
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""

class Complex:
    """
    Класс «Комплексное число»
    """
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    
    def __add__(self, other:"Complex") -> "Complex":
        return Complex(self.__a + other.__a, self.__b + other.__b)

    def __sub__(self, other:"Complex") -> "Complex":
        return Complex(self.__a - other.__a, self.__b - other.__b)

    def __mul__(self, other:"Complex") -> "Complex":
        return Complex(self.__a * other.__a + self.__b * other.__b * (-1), self.__b * other.__a + self.__a * other.__b)

    def __str__(self):
        return f'{self.__a}{"" if self.__b < 0 else "+"}{self.__b}i'

if __name__ == "__main__":
    c1 = Complex(2,3)
    c2 = Complex(4,-5)
    c3 = c1+c2
    assert str(c3) == "6-2i", "Сложение неверно"

    c3 = Complex(1,-1)
    c4 = Complex(3,6)
    assert str(c3*c4) == "9+3i", "Умножение неверно"