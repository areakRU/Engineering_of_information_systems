from abc import ABCMeta, abstractmethod

class IChair(metaclass = ABCMeta):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def sit_on(self):
        pass


class ISofa(metaclass = ABCMeta):
    @abstractmethod
    def has_legs(self):
        pass

    @abstractmethod
    def lie_on(self):
        pass


class IFurnitureFactory(metaclass = ABCMeta):
    @abstractmethod
    def create_chair(self) -> IChair:
        pass

    @abstractmethod
    def create_sofa(self) -> ISofa:
        pass


class ModernFurnitureFactory(IFurnitureFactory):
    def create_chair(self) -> IChair:
        return ModernChair()

    def create_sofa(self) -> ISofa:
        return ModernSofa()


class VictorianFurnitureFactory(IFurnitureFactory):
    def create_chair(self) -> IChair:
        return VictorianChair()

    def create_sofa(self) -> ISofa:
        return VictorianSofa()


class ModernChair(IChair):
    def has_legs(self):
        print('Has no legs')

    def sit_on(self):
        print('You\'re sitting on it')


class VictorianChair(IChair):
    def has_legs(self):
        print('Has four legs')

    def sit_on(self):
        print('You\'re sitting on it')


class ModernSofa(ISofa):
    def has_legs(self):
        print('Has no legs')

    def sit_on(self):
        print('You\'re lying on it')


class VictorianSofa(ISofa):
    def has_legs(self):
        print('Has four legs')

    def sit_on(self):
        print('You\'re lying on it')


if __name__ == '__main__':
    factory: IFurnitureFactory = VictorianFurnitureFactory()
    chair: IChair = factory.create_chair()
    chair.has_legs()