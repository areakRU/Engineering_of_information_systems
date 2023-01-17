from abc import ABCMeta, abstractmethod

class IStrategy(metaclass = ABCMeta):
    @abstractmethod
    def make_route(self):
        pass


class Navigator:
    def __init__(self):
        self.__strategy = None

    def set_strategy(self, strategy: IStrategy):
        self.__strategy = strategy

    def make_route(self):
        if self.__strategy != None:
            self.__strategy.make_route()


class CarStrategy(IStrategy):
    def make_route(self):
        print('Car route was maded!')


class PedestrianStrategy(IStrategy):
    def make_route(self):
        print('Pedestrian route was maded!')


if __name__ == '__main__':
    navigator = Navigator()
    car_strategy = CarStrategy()
    pedestrian_strategy = PedestrianStrategy()

    navigator.set_strategy(car_strategy)
    navigator.make_route()

    navigator.set_strategy(pedestrian_strategy)
    navigator.make_route()