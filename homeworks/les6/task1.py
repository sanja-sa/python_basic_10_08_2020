"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


from threading import Thread, Event, Timer
import time

class TrafficLight:
    """
    Класс светофора
    """
    # Рабочая схема светофора
    __work_sheme = (("red", 7), ("yellow", 2), ("green", 5))
    # Текущее состояние светофора
    __color = ()

    def __init__(self):
        self.__th = Thread(target=self.__thread_run)
        self.__state = 0
        self.__flag = True
        self.__stop_ev = Event()
        self.___update_color()
    
    def stop(self):
        """
        Остановка работы светофора
        """
        print("TrafficLight want to stop")
        self.__stop_ev.set()

    def running(self):
        """
        Запуск светофора
        """
        self.__th.start()
        self.__th.join()

    def __trigger(self):
        """
        Переключение на следующий по логике цвет
        """
        self.__state = self.__state + 1 if self.__flag else self.__state - 1
        self.__flag = not self.__flag if self.__state == 2 or self.__state == 0 else self.__flag

    def __thread_run(self):
        """
        Метод потока светофора
        """
        while not self.__stop_ev.wait(self.__color[1]):
            self.__trigger()
            self.___update_color()

    def ___update_color(self):
        """
        Установка цвета по состоянию
        """
        self.__color = self.__work_sheme[self.__state]
        print(f"Current color: {self.__color[0]}")

tf1 = TrafficLight()
stop_timer = Timer(30, tf1.stop)
stop_timer.start()
tf1.running()
