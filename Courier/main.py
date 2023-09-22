import Courier_on_bike
import Courier_on_car
import Courier_on_foot
import Order
import time 
import keyboard

all_couriers = [    ]
orders = [  ]
earnings = 0
factor = 1

print("Программа: \"Курьер\".")

print("Введите коэффициент ускорения времени: ")
factor = int(input())                               #Задаёт значение коэффициента, который определяет во сколько раз время в системе
                                                                                                                # быстрее реального времени
print("Введите количество курьеров-пешеходов:")
num_of_courier_on_foot = int(input())
for i in range(0, num_of_courier_on_foot):
    print("Введите координаты местоположения курьера-пешехода № " + str(len(all_couriers)) + " через пробел")
    x, y = map(int, input().split()) 
    courier = Courier_on_foot.Courier_on_foot(len(all_couriers), x, y, factor)
    all_couriers.append(courier)

print("Введите количество курьеров на велосипедах:")
num_of_courier_on_bike = int(input())                                                   #Определение курьеров
for i in range(0, num_of_courier_on_bike):
    print("Введите координаты местоположения курьера-велосипедиста № " + str(len(all_couriers)) + " через пробел")
    x, y = map(int, input().split()) 
    courier = Courier_on_bike.Courier_on_bike(len(all_couriers), x, y, factor)
    all_couriers.append(courier)

print("Введите количество курьеров-автомобилистов:")
num_of_courier_on_car = int(input())
for i in range(0, num_of_courier_on_car):
    print("Введите координаты местоположения курьера-автомобилиста № " + str(len(all_couriers)) + " через пробел")
    x, y = map(int, input().split()) 
    courier = Courier_on_car.Courier_on_car(len(all_couriers), x, y, factor)
    all_couriers.append(courier)

print("Введите исходное количество заказов:")
num_of_start_orders = int(input())                              #Ввод исходных заказов
for i in range(0, num_of_start_orders):
    print("Введите координаты отправителя заказа № " + str(i+1) + " через пробел")
    x, y = map(int, input().split()) 
    print("Введите координаты доставки заказа № " + str(i+1)   + " через пробел")
    x1, y1 = map(int, input().split()) 
    print("Введите цену заказа № " + str(i+1))
    price = int(input())
    order = Order.Order(i+1, x, y, price, x1, y1)
    orders.append(order)

def give_order(courier):
    #Определяет курьеру ближайший заказ
    coord = courier.get_coord()
    nearest_order = orders[0]
    for i in range(1, len(orders)):
        order = orders[i]
        if order.count_distance(coord) < nearest_order.count_distance(coord):
            nearest_order = order
    orders.remove(nearest_order)
    print("Заказ № " + str(nearest_order.get_id()) + " взят в доставку.")
    return nearest_order

IsAlive = True

def terminate():
    global IsAlive
    IsAlive = False
    print("Работа программы была прервана.")
    print("Прибыль: " + str(earnings))
keyboard.add_hotkey('esc', terminate)

def add_order():
    print("Введите координаты отправителя заказа № " + str(len(orders))  + " через пробел")
    x, y = map(int, input().split()) 
    print("Введите координаты доставки заказа № " + str(len(orders)) + " через пробел")   #Добавляет заказ во время работы программы
    x1, y1 = map(int, input().split()) 
    print("Введите цену заказа № " + str(len(orders)))
    price = int(input())
    order = Order.Order(len(orders), x, y, price, x1, y1)
    orders.append(order)
keyboard.add_hotkey('a', add_order)

def add_courier():
    print("Введите 1, чтобы добавить нового пешего курьера, 2, чтобы добавить нового курьера-велосипедиста, 3 - курьера автомобилиста")
    n = int(input())
    if n == 1:                                              #Добавляет курьеров во время исполнения программы
        print("Введите местоположение курьера-пешехода № " + str(len(all_couriers)) + " через пробел")
        x, y = map(int, input().split()) 
        courier = Courier_on_foot.Courier_on_foot(len(all_couriers), x, y, factor)
        all_couriers.append(courier)
    elif n == 2:
        print("Введите местоположение курьера-велосипедиста № " + str(len(all_couriers)) + " через пробел")
        x, y = map(int, input().split()) 
        courier = Courier_on_bike.Courier_on_bike(len(all_couriers), x, y, factor)
        all_couriers.append(courier)
    elif n ==3:
        print("Введите местоположение курьера-автомобилиста № " + str(len(all_couriers)) + " через пробел")
        x, y = map(int, input().split())
        courier = Courier_on_car.Courier_on_car(len(all_couriers),x, y, factor)
        all_couriers.append(courier)
keyboard.add_hotkey('c', add_courier)

print("Дополнительные команды управления программой:")
print("a - добавить заказ, c - добавить курьера, esc - прервать работу программы")

while IsAlive:
    for i in range(0, len(all_couriers)):
        courier = all_couriers[i]
        if courier.isFree() and len(orders) != 0:
            courier.set_order(give_order(courier))  #Если курьер свободен, назначает ему заказ
            print("Ориентировочное время доставки: " + str(round((courier.get_time_of_free() - time.time())/60)) + " минут(a)(ы).")
        elif courier.get_time_of_free() <= time.time() and not(courier.isFree()):
            courier.set_coord(courier.get_order().get_destination()[0], courier.get_order().get_destination()[1]) 
            earnings += courier.get_earning()       #Если курьер доставил заказ, определяет курьера в системе, как свободного.
            courier.setFree()
            print("Заказ № " + str(courier.get_order().get_id())+ " доставлен.")
            print("Прибыль от заказа: " + str(courier.get_earning()))
    if len(orders) == 0:
        all_free = True
        for courier in all_couriers:
            if not(courier.isFree()):
                all_free = False        
        if all_free:                            #Если все заказы доставлены, то программа заканчивается, выводя выручку от доставки всех заказов.
            print("Все заказы доставлены.")
            print("Прибыль: " + str(earnings))
            break