import Courier
class Courier_on_foot(Courier.Courier):
    __salary = 150 #рублей
    __speed = 5 #км/ч
    
    def get_speed(self):
        return self.__speed
    
    def get_salary(self):
        return self.__salary
