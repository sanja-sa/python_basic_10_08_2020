"""
Начните работу над проектом «Склад оргтехники». 
Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


from enum import Enum
from task3 import OnlyDigitException

class Input:
    """
    Класс утилита для ввода и проверки данных
    """
    @staticmethod
    def input_data(param_name, param_type, param_from = None, param_to = None):
        """
        Получаем данные от пользователя
        :param param_name: Текстовое обозначение параметра
        :param param_type: Тип параметра
        :return: Результат принятого параметра
        """
        while True:
            try:
                param = param_type(input(f'Введите "{param_name}": '))

                if param_from != None and type(param_from) is list:
                    if param not in param_from:
                        print(f'"{param_name}" должно быть в пределе {param_from}')    
                        continue
                else:
                    if param_from != None and param < param_from:
                        print(f'"{param_name}" должно быть более равно {param_from}')    
                        continue
                    if param_to != None and param > param_to:
                        print(f'"{param_name}" должно быть менее равно {param_to}')
                        continue
            except:
                print(f'"{param_name}" должно быть как {param_type}')
                continue
            break
        return param


class Interface(Enum):
    """
    Класс перечисление интерфейса подключения к компьютеру
    """
    USB = 0
    LAN = 1


class Color(Enum):
    """
    Класс перечисление цветности объекта
    """
    Color = 0
    BW = 1
    CMYK = 2


class OfficeEquipment:
    """
    Класс Офисное оборудование
    """
    def __init__(self, model_name):
        self.__model_name =  model_name
        
    @property
    def model(self):
        return self.__model_name

    def __str__(self):
        return self.__model_name
        

class Stock:
    """
    Класс склад
    """
    # В данном случае склад один ( можно несколько складов сделать заменить __instance на tuple )
    __instance = None
    # Склад оборудования 'Модель' : {'Количество': cnt, 'Объект' : cls }
    __equipment = {}

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @classmethod
    def add_to_stock(cls, obj, cnt):
        """
        Добавить продукт на склад
        :param obj: Объект
        :param cnt: Количество объекта
        """
        OnlyDigitException().is_digit(cnt)
        if obj.model in cls.__equipment:
            cls.__equipment[obj.model]['Количество'] += cnt
        else:
            cls.__equipment[obj.model] = {'Количество' : cnt, 'Объект': obj}

    @classmethod
    def remove_from_stock(cls, obj, cnt):
        """
        Удалить продукт со склада
        :param obj: Объект
        :param cnt: Количество объекта
        """
        OnlyDigitException().is_digit(cnt)
        if obj.model in cls.__equipment:
            count = cls.__equipment[obj.model]['Количество']
            cls.__equipment[obj.model]['Количество'] = 0 if count <= cnt else count - cnt

    def __str__(self):
        out = ""
        for model in self.__equipment:
            out += f'{model} ({self.__equipment[model]["Объект"]}) - {self.__equipment[model]["Количество"]} шт.\n'
        return out

    def __getitem__(self, model):
        return self.__equipment[model]


class Printer(OfficeEquipment):
    """
    Класс принтер
    """
    def __init__(self, model, is_laser:bool=False, interface:"Interface"=Interface.USB):
        super().__init__(model)
        self.__is_laser = is_laser
        self.__interface = interface

    def __str__(self):
        return f'Принтер, Лазерный: {self.__is_laser}. Интерфейс: {self.__interface.name}'

    def input_custom_data(self):
        """
        Получить и проверить данные со входа
        """
        self.__is_laser = Input.input_data(f"Принтер лазерный? ( Д / Н ): ", str, ["Д","Н"]) == "Д"
        self.__interface = Interface(Input.input_data(f"Интерфейс подключения к PC: 0: USB, 1: LAN", int, 0, 1))


class Scanner(OfficeEquipment):
    """
    Класс сканер
    """
    def __init__(self, model, diagonal_size:int=0, interface:"Interface"=Interface.USB):
        super().__init__(model)
        self.__diagonal_size = diagonal_size
        self.__interface = interface

    def __str__(self):
        return f'Сканер, Рабочая диагональ: {self.__diagonal_size}. Интерфейс: {self.__interface.name}'

    def input_custom_data(self):
        """
        Получить и проверить данные со входа
        """
        self.__diagonal_size = Input.input_data(f"Размер диагонали:", int, 10, 1000)
        self.__interface = Interface(Input.input_data(f"Интерфейс подключения к PC: 0: USB, 1: LAN", int, 0, 1))


class Copier(OfficeEquipment):
    """
    Класс ксерокс
    """
    def __init__(self, model, copie_per_sec:int=0, color:"Color"=Color.BW):
        super().__init__(model)
        self.__copie_per_sec = copie_per_sec
        self.__color = color

    def __str__(self):
        return f'Ксерокс, Копий в секунду: {self.__copie_per_sec}. Цветность: {self.__color.name}'

    def input_custom_data(self):
        """
        Получить и проверить данные со входа
        """
        self.__copie_per_sec = Input.input_data(f"Количество копий:", int, 10, 1000)
        self.__сolor = Color(Input.input_data(f"Цветность: 0: Цветной, 1: ЧБ, 2: CMYK", int, 0, 2))


types_product = (("Принтер",Printer), ("Сканер",Scanner), ("Ксерокс",Copier))
while True:
    model_name = Input.input_data("Название продукта", str)

    choose_type_str = ""
    for idx,val in enumerate(types_product):
        choose_type_str += f'{idx}: {val[0]}, '
    type_product = Input.input_data(f"Тип продукта: {choose_type_str[:-2]}", int, 0, len(types_product)-1)

    obj = types_product[type_product][1](model_name)
    obj.input_custom_data()
    print(f'Создан продукт: {obj}')

    yes = Input.input_data(f"Добавить продукты на склад ( Д / Н ): ", str, ["Д","Н"])
    if yes == "Д":
        cnt_product = Input.input_data(f"Количество продукта пришло на склад: ", int, 1)
        Stock.add_to_stock(obj, cnt_product)
    else:
        cnt_product = Input.input_data(f"Количество продукта ушло со склада: ", int, 1)
        Stock.remove_from_stock(obj, cnt_product)

    yes = Input.input_data(f"Распечатать склад ( Д / Н ): ", str, ["Д","Н"])
    if yes == "Д":
        print(Stock())

    yes = Input.input_data(f"Продолжить ввод нового продукта? ( Д / Н ): ", str, ["Д","Н"])
    if yes == "Д":
        continue
    break
