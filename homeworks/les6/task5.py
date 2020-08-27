"""
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    """
    Класс канцелярской принадлежности
    """
    def __init__(self, title):
        self.__title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    """
    Класс ручка
    """
    def draw(self):
        print("Запуск отрисовки ручкой.")

class Pencil(Stationery):
    """
    Класс карнадаш
    """
    def draw(self):
        print("Запуск отрисовки карандашом.")

class Handle(Stationery):
    """
    Класс маркер
    """

    def draw(self):
        print("Запуск отрисовки маркером.")

instrument = Handle("заголовок")
instrument.draw()
instrument = Pencil("Что-то отрисовать")
instrument.draw()
instrument = Pen("Что-то отрисовать ручкой")
instrument.draw()