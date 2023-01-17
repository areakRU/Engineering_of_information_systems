from abc import ABCMeta, abstractmethod

class ClientInterface(metaclass = ABCMeta):
    def make_sth(self, data):
        pass


class Service:
    def make_sth(self, special_data: str):
        print('Service is making sth with special data...')


class Adapter(ClientInterface):
    def __init__(self, adaptee: Service):
        self.adaptee = adaptee

    def convert_to_special_data(self, data: str) -> str:
        return data + ' special'

    def make_sth(self, data: str):
        special_data = self.convert_to_special_data(data)
        self.adaptee.make_sth(special_data)


if __name__ == '__main__':
    service = Service()
    adapter = Adapter(service)
    adapter.make_sth('data')