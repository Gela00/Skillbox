class Transport():
    def __init__(self, *args, **kwargs):
        self._coordinates = (args[0], args[1])
        self._speed = args[2]
        self._brand = args[3]
        self._year = args[4]
        self._number = args[5]

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number


    def __str__(self):
        '''
        Представление всей информации для вывода
        '''
        return f'{self.coordinates}, {self.speed}, {self.brand}, {self.year}, {self.number}'


    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        x, y = self.coordinates
        if (pos_x <= x <= pos_x + length and pos_y <= y <= pos_y + width):
            return True
        return False


class Passenger():
    def __init__(self, *args, **kwargs):
        self._passengers_capacity = args[0]
        self._number_of_passengers = args[1]

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers

class Cargo():
    def __init__(self, *args, **kwargs):
        self._carrying = carrying

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, *args):
        self._height = args[0]
        Transport.__init__(*args[1::]) #вызываем родительский метод в дочернем

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


class Auto(Transport):
    def __init__(self, *args, **kwargs):
        self._brand = args[0]
        Transport.__init__(*args[1::])

    @property
    def factory(self):
        return self._brand

    @factory.setter
    def factory(self, factory):
        self._brand = brand


class Ship(Transport):
    def __init__(self, *args, **kwargs):
        self._port = args[0]
        Transport.__init__(*args[1::])

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port


class Car(Auto):
    def __init__(self, brand, *args):
        self._brand = brand
        Auto.__init__(*args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class Bus(Auto, Passenger):
    def __init__(self, brand, passengers_capacity, number_of_passengers, *auto_args):
        self._brand = brand
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Auto.__init__(self, *auto_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class CargoAuto(Auto, Cargo):
    def __init__(self, brand, carrying, *auto_args):
        self._brand = brand
        Cargo.__init__(self, carrying)
        Auto.__init__(self, *auto_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class Boat(Ship):
    def __init__(self, brand, *ship_args):
        self._brand = brand
        Ship.__init__(*ship_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class PassengerShip(Ship, Passenger):
    def __init__(self, brand, passengers_capacity, number_of_passengers, *ship_args):
        self._brand = brand
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Ship.__init__(self, *ship_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class CargoShip(Ship, Cargo):
    def __init__(self, brand, carrying, *ship_args):
        self._brand = brand
        Cargo.__init__(self, carrying)
        Ship.__init__(self, *ship_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class Airplane(Plane):
    def __init__(self, brand, *plane_args):
        self._brand = brand
        Plane.__init__(*plane_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class PassengerPlane(Plane, Passenger):
    def __init__(self, brand, passengers_capacity, number_of_passengers, *plane_args):
        self._brand = brand
        Passenger.__init__(self, passengers_capacity, number_of_passengers)
        Plane.__init__(self, *plane_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class CargoPlane(Plane, Cargo):
    def __init__(self, brand, carrying, *plane_args):
        self._brand = brand
        Cargo.__init__(self, carrying)
        Plane.__init__(self, *plane_args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand


class Seaplane(Plane, Ship):
    def __init__(self, brand, port, height, *args):
        self._brand = brand
        Ship._port = port
        Plane._height = height
        Transport.__init__(self, *args)

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand