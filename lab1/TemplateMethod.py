from abc import ABCMeta, abstractmethod

class House(metaclass = ABCMeta):
    def template_method(self):
        self.make_foundation()
        self.make_walls()
        self.make_roof()
        self.make_doors()
        self.make_windows()

    def make_foundation(self):
        print('Foundation is made!')

    def make_walls(self):
        print('Walls are made!')

    def make_roof(self):
        print('Roof is made!')

    def make_doors(self):
        print('Doors are made!')

    def make_windows(self):
        print('Windows are made!')


class WillageHouse(House):
    def make_roof(self):
        print('Triangular roof is made!')


class BoxHouse(House):
    def make_roof(self):
        print('Flat roof is made!')


if __name__ == '__main__':
    willage_house = WillageHouse()
    willage_house.template_method()
    print('------------------------')
    box_house = BoxHouse()
    box_house.template_method()