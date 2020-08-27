"""
Реализовать базовый класс Worker (работник), 
в котором определить атрибуты: name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, 
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """
    Класс работника
    """
    _income = {"wage":0, "bonus":0}

    def __init__(self, **kwargs):        
        # Имя работника
        self.name = kwargs["name"] if "name" in kwargs else ""
        # Фамилия работника
        self.surname = kwargs["surname"] if "surname" in kwargs else ""
        # Должность работника
        self.position = kwargs["position"] if "position" in kwargs else "Worker"
        # Доход работника
        self._income["wage"] = kwargs["wage"] if "wage" in kwargs else 0
        self._income["bonus"] = kwargs["bonus"] if "wage" in kwargs else 0

class Position(Worker):
    """
    Класс расчетов данных сотрудников исходя из должности
    """
    _position_sheme = {"Director":5,"Manager":3,"Worker":2,"Slave":0}
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.position = self.position if self.position in self._position_sheme else "Worker"

    def get_full_name(self) -> str:
        """
        Получение полного имени сотрудника
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self) -> float:
        """
        Получить доход сотрудника
        """
        return self._income["wage"] + (self._income["bonus"] * self._position_sheme[self.position])


worker1 = Position(name = "Ваня", surname = "Вередлон", wage = 2000, bonus = 500)
print(worker1.get_full_name())
print(worker1.get_total_income())


assert worker1.get_full_name() == "Ваня Вередлон", "Проблема с именами сотрудника"
assert worker1.get_total_income() == 3000, "Проблема с расчетом дохода"