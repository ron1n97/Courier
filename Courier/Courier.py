import Order
from math import sqrt
import time

class Courier:
    __current_order = None
    __isFree = True
    __time_of_free = 0
    __path = 0
    __time_of_start = None

    def __init__(self, id, x, y, factor):
        self.id = id
        self.coord = [x, y]
        self.__factor = factor

    def get_factor(self):
        return self.__factor

    def get_time_of_free(self):
        return self.__time_of_free
    
    def set_coord(self, x, y):
        self.coord = [x, y]

    def get_coord(self):
        return self.coord
    
    def isFree(self):
        return self.__isFree
    
    def setFree(self):
        self.__isFree = True
    
    def set_path(self):
        x = self.get_coord()[0]
        y = self.get_coord()[1]
        x0 = self.get_order().get_coord()[0]
        y0 = self.get_order().get_coord()[1]            #Определяет длину пути курьера для выполнения заказа
        x1 = self.get_order().get_destination()[0]
        y1 = self.get_order().get_destination()[1]
        self.__path = sqrt((x0-x)**2 + (y0-y)**2) + sqrt((x1-x0)**2 + (y1-y0)**2)
    
    def get_path(self):
        return self.__path
    
    def get_speed(self):
        pass
    
    def get_salary(self):
        pass
    
    def get_time_of_start(self):
        return self.__time_of_start
    
    def set_time_of_free(self):     #время движения в секундах (учитывая можитель времени)      +    время начало выполнения заказа
        self.__time_of_free = (self.get_path()/self.get_speed()*3600/self.get_factor() + self.get_time_of_start())

    def get_earning(self):
        return self.get_order().get_price() - self.get_salary()
    
    def get_time_of_free(self):
        return self.__time_of_free

    def set_order(self, order):
        self.__current_order = order      #получает заказ + ставится время выполнения заказа <-> время освобождения курьера 
        self.__time_of_start = time.time()      # и путь до точки отправки + путь до доставки
        self.__isFree = False
        self.set_path()
        self.set_time_of_free()

    def get_order(self):
        return self.__current_order
        

