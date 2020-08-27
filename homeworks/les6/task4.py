"""
Реализуйте базовый класс Car. 
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
"""


class Car:
    """
    Базовый класс авто
    """
    # Текущая скорость автомобиля
    speed = 0

    def __init__(self, **kwargs):  
        self.color=kwargs["color"] if "color" in kwargs else "red"
        self.name=kwargs["name"] if "name" in kwargs else ""
        self.is_police = kwargs["is_police"] if "is_police" in kwargs else False
        print(f'Авто имя:{self.name} цвет:{self.color} полиц.:{self.is_police} сконструирована. Тип авто: {self.__class__.__name__}')

    def go(self):
        """
        Меняем статус авто: Движение
        """
        print(f'Авто {self.name} поехала.')

    def stop(self):
        """
        Меняем статус авто: Остановка
        """
        print(f'Авто {self.name} остановилась.')

    def turn(self, direction="Направо"):
        """
        Меняем статус поворота авто
        """
        print(f'Авто {self.name} повернула "{direction}".')

    def show_speed(self):
        """
        Показ текущей скорости авто
        """
        print(f'Текущая скорость авто {self.speed}.')

class TownCar(Car):
    """
    Класс городской машины
    """
    def __init__(self, **kwargs):    
        super().__init__(**kwargs)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Скорость слишком велика для данного авто!!!.')

class SportCar(Car):
    """
    Класс спортивной машины
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class WorkCar(Car):
    """
    Класс рабочей машины
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Скорость слишком велика для данного авто!!!.')

class PoliceCar(Car):
    """
    Класс полицейской машины
    """
    def __init__(self, **kwargs):
        kwargs["is_police"] = True
        super().__init__(**kwargs)        
        
# TODO: Работать через фабрику
police1 = PoliceCar(name="к123оп", color="blue")
tow1 = TownCar(name="б321як", color="gray")
work1 = WorkCar(name="к213яб", color="black")

tow1.speed = 100
tow1.show_speed()

tow1.speed = 50
tow1.show_speed()

work1.go()
tow1.stop()