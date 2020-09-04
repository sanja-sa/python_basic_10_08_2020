"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    """
    Класс отвечающий за работу с датами
    """
    def __init__(self, fmt_date: str):
        self.parse(fmt_date)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def date(self):
        return [self.__day, self.__month, self.__year]

    @classmethod
    def parse(cls, fmt_date: str) -> list:
        """
        Парсер даты из строки
        :param fmt_date: Строка даты в формате '22-12-2020'
        """
        try:
            day, month, year = fmt_date.split("-")
            cls.__day, cls.__month, cls.__year = int(day), int(month), int(year)
        except:
            raise ValueError("Формат даты должен сочтоять из чисел числовой 'dd-mm-year'")

    @staticmethod
    def valid(day:int, month:int, year:int) -> bool:
        """
        Проверка на валидность данных даты
        :param day: Число
        :param month: Месяц
        :param year: Год
        :return : True - если данные даты валидны 
        """
        # TODO: проверить на реальность даты через функции календаря
        if day < 1 or day > 31:
            return False 
        elif month < 1 or month > 12:
            return False
        elif year < 1:
            return False
        return True

if __name__ == "__main__":
    dt = Date("23-12-2322")
    assert Date.valid(dt.day,dt.month,dt.year), "Проверка валидности некорректна" 
    dt = Date("0-12-2020")
    assert not Date.valid(dt.day,dt.month,dt.year), "Проверка невалидности некорректна" 

    dt.day = 11
    dt.month = 33
    dt.year = 2020
    assert not Date.valid(dt.day,dt.month,dt.year), "Проверка невалидности и ручной ввод даты некорректна" 