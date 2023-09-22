import Courier
class Courier_on_bike(Courier.Courier):
    __salary = 160 #рублей
    __speed = 10 #км/ч
    
    def get_speed(self):
        return self.__speed
    
    def get_salary(self):
        return self.__salary