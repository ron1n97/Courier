import Courier
import math 
class Courier_on_car(Courier.Courier):
    __km_bonus = 20 #рублей
    __salary = 140 #рублей
    __speed = 45 #км/ч

    def get_km_bonus(self):
        return self.__km_bonus
    
    def get_speed(self):
        return self.__speed
    
    def get_salary(self):
        return self.__salary

    def get_earning(self):          #переопределение метода рассчета прибыли, учитывая бонус за километраж
        return self.get_order().get_price() - self.get_salary() - math.floor(self.get_path())*self.get_km_bonus()
    