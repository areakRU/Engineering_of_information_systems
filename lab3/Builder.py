from abc import ABCMeta, abstractmethod

class CarBuilder: pass

class Car:
    def __init__(self):
        self.count_of_wheels: int = None
        self.count_of_seats: int = None
        self.type_of_rubber: str = None
        self.type_of_transmission: str = None
        self.type_of_engine: str = None
        self.is_car_spoiler: bool = None

    def print_parameters(self):
        print('count_of_wheels: ', self.count_of_wheels)
        print('count_of_seats: ', self.count_of_seats)
        print('type_of_rubber: ', self.type_of_rubber)
        print('type_of_transmission: ', self.type_of_transmission)
        print('type_of_engine: ', self.type_of_engine)
        print('is_car_spoiler: ', self.is_car_spoiler)

        
class ICarBuilder(metaclass = ABCMeta):
    @abstractmethod
    def set_count_of_wheels(self, count: int):
        pass

    @abstractmethod
    def set_count_of_seats(self, count: int):
        pass

    @abstractmethod
    def set_type_of_rubber(self, type: str):
        pass

    @abstractmethod
    def set_type_of_transmission(self, type: str):
        pass

    @abstractmethod
    def set_type_of_engine(self, type: str):
        pass

    @abstractmethod
    def set_car_spoiler(self, is_spoiler: bool):
        pass


class CarBuilder(ICarBuilder):
    def __init__(self):
        self.__car = Car()

    def __reset(self):
        self.__car = Car()

    def set_count_of_wheels(self, count: int) -> CarBuilder:
        self.__car.count_of_wheels = count
        return self

    def set_count_of_seats(self, count: int) -> CarBuilder:
        self.__car.count_of_seats = count
        return self

    def set_type_of_rubber(self, type: str) -> CarBuilder:
        self.__car.type_of_rubber = type
        return self

    def set_type_of_transmission(self, type: str) -> CarBuilder:
        self.__car.type_of_transmission = type
        return self

    def set_type_of_engine(self, type: str) -> CarBuilder:
        self.__car.type_of_engine = type
        return self

    def set_car_spoiler(self, is_spoiler: bool) -> CarBuilder:
        self.__car.is_car_spoiler = is_spoiler
        return self

    def get_car(self) -> Car:
        product = self.__car
        self.__reset()
        return product


if __name__ == '__main__':
    builder: CarBuilder = CarBuilder()
    car: Car = builder.set_count_of_seats(2)\
                        .set_count_of_wheels(4)\
                        .set_type_of_transmission('manual')\
                        .set_type_of_engine('super power engine')\
                        .set_type_of_rubber('rubber for sport car')\
                        .set_car_spoiler(True)\
                        .get_car()

    car.print_parameters()