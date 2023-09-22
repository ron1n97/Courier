import time
from math import sqrt

class Order(object):

    def __init__(self, id, x0, y0, price, x1, y1):
        self.id = id
        self.coord = [x0, y0]
        self.dest = [x1, y1]
        self.price = price
        self.dispatch_time = time.time()

    def get_coord(self):
        return self.coord
    
    def get_price(self):
        return self.price
    
    def get_time(self):
        return self.dispatch_time
    
    def get_destination(self):
        return self.dest
    
    def get_id(self):
        return self.id
    
    def count_distance(self, coord):        #рассчитывает расстояние от курьера до заказа
        distance = sqrt((self.get_coord()[0] - coord[0])**2 + (self.get_coord()[1] - coord[1])**2)
        return distance
    
