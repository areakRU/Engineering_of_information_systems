from abc import ABCMeta, abstractmethod

class PrivateHouse: pass
class CoffeeShop: pass
class Bank: pass

class IVisitor(metaclass= ABCMeta):
    @abstractmethod
    def give_private_house_insurance(self, building: PrivateHouse):
        pass

    @abstractmethod
    def give_coffee_shop_insurance(self, building: CoffeeShop):
        pass

    @abstractmethod
    def give_bank_insurance(self, building: Bank):
        pass


class Visitor(IVisitor):
    def give_private_house_insurance(self, building: PrivateHouse):
        print('Insurance is given to a private house!')

    def give_coffee_shop_insurance(self, building: CoffeeShop):
        print('Insurance is given to a coffee shop!')

    def give_bank_insurance(self, building: Bank):
        print('Insurance is given to a bank!')


class PrivateHouse:
    def accept(self, v: IVisitor):
        v.give_private_house_insurance(self)


class CoffeeShop:
    def accept(self, v: IVisitor):
        v.give_coffee_shop_insurance(self)


class Bank:
    def accept(self, v: IVisitor):
        v.give_bank_insurance(self)


if __name__ == '__main__':
    visitor = Visitor()
    house = PrivateHouse()
    shop = CoffeeShop()
    bank = Bank()

    house.accept(visitor)
    shop.accept(visitor)
    bank.accept(visitor)