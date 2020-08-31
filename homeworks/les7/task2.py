"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 
Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, 
проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod

class Clothes:
    """
    Базовый класс одежды
    """
    # Объект списка доступной одежды для текущей работы
    __all_clothes = []

    def __init__(self, name):
        # Название одежды
        self.__name = name
        self.__all_clothes.append(self)
    
    @abstractmethod
    def tissue_consumption(self):
        """
        Расчет расхода ткани на одежду
        """
        pass

    @classmethod
    def all_tissue_consumption(cls):
        """
        Расчет общего расхода ткани на созданные объекты одежды
        """
        all_consumption = 0
        for cloth in cls.__all_clothes:
            all_consumption += cloth.tissue_consumption()
        return all_consumption


class Coat(Clothes):
    """
    Класс пальто
    """
    # Размер пальто
    V = 0

    @property
    def size(self):
        """
        Получить размер пальто
        """
        return self.V
    
    @size.setter
    def size(self, size):
        """
        Установить размер пальто
        """
        self.V = size

    def tissue_consumption(self):
        return (self.V/6.5 + 0.5)


class Costume(Clothes):
    """
    Класс костюм
    """
    # Рост костюма
    H = 0

    @property
    def height(self):
        """
        Получить рост пальто
        """
        return self.H
    
    @height.setter
    def height(self, height):
        """
        Установить рост пальто
        """
        self.H = height

    def tissue_consumption(self):
        return (2 * self.H + 0.3)


coat1 = Coat("Модель 123")
coat1.size = 130
print(coat1.tissue_consumption())
coat2 = Coat("Модель 234")
coat2.size = 195
print(coat2.tissue_consumption())
cost1 = Costume("Модель 098")
cost1.size = 678
print(cost1.tissue_consumption())
cost2 = Costume("Модель 890")
cost2.size = 876
print(cost2.tissue_consumption())

print(Clothes.all_tissue_consumption())