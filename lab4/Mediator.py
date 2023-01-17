from abc import ABCMeta, abstractmethod

class Person: pass

class Mediator(metaclass = ABCMeta):
    @abstractmethod
    def notify(self, sender: Person):
        pass


class SpecificMediator(Mediator):
    def __init__(self):
        self.programmer: Programmer = None
        self.tester: Tester = None
        self.manager: Manager = None

    def notify(self, sender: Person):
        if type(sender) == Programmer:
            self.react_on_programmer()
        if type(sender) == Tester:
            self.react_on_tester()
        if type(sender) == Manager:
            self.react_on_manager()

    def react_on_programmer(self):
        self.tester.received_message = 'Program is done.'

    def react_on_tester(self):
        self.manager.received_message = 'Program is tested.'

    def react_on_manager(self):
        self.programmer.received_message = 'Well done!'
        self.tester.received_message = 'Well done!'


class Person(metaclass = ABCMeta):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self.received_message = None


class Programmer(Person):
    def job_is_done(self):
        self.mediator.notify(self)


class Tester(Person):
    def job_is_done(self):
        self.mediator.notify(self)


class Manager(Person):
    def job_is_done(self):
        self.mediator.notify(self)


def print_messages(persons: tuple[Person]):
    for person in persons:
        print(person.received_message)
    print('--------------')


if __name__ == '__main__':
    mediator: Mediator = SpecificMediator()

    programmer: Programmer = Programmer(mediator)
    tester: Tester = Tester(mediator)
    manager: Manager = Manager(mediator)

    mediator.programmer = programmer
    mediator.tester = tester
    mediator.manager = manager

    print_messages((programmer, tester, manager))
    programmer.job_is_done()
    print_messages((programmer, tester, manager))
    tester.job_is_done()
    print_messages((programmer, tester, manager))
    manager.job_is_done()
    print_messages((programmer, tester, manager))