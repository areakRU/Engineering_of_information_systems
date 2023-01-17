from abc import ABCMeta, abstractmethod
import copy

class IIterator(metaclass = ABCMeta):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_more(self):
        pass


class ITreeCollection(metaclass = ABCMeta):
    @abstractmethod
    def get_left_right_iterator(self) -> IIterator:
        pass

    def get_right_left_iterator(self) -> IIterator:
        pass

    def set_left(self, subtree):
        pass

    def set_right(self, subtree):
        pass
 

class TreeCollection(ITreeCollection):
    def __init__(self, data):
        self.data = data
        self.left: TreeCollection = None
        self.right: TreeCollection = None

    def get_left_right_iterator(self) -> IIterator:
        return LeftRightIterator(self)

    def get_right_left_iterator(self) -> IIterator:
        return RightLeftIterator(self)


class LeftRightIterator(IIterator):
    def __init__(self, collection: TreeCollection):
        self.collection = collection
        self.stack = list()
        self.tree_array = list()
        self.current_element = -1
        self.__build_tree_array()

    def get_next(self):
        self.current_element += 1
        return self.tree_array[self.current_element]

    def has_more(self):
        return self.current_element < len(self.tree_array)

    def __build_tree_array(self):
        current_element: TreeCollection = copy.deepcopy(self.collection)
        self.stack.append(current_element)
        self.stack.append(current_element)
        while True:
            if len(self.stack) == 0:
                break

            current_element = self.stack.pop()

            while current_element != None:
                if current_element.data not in self.tree_array:
                    self.tree_array.append(current_element.data)

                if current_element.left != None and current_element.left.data not in self.tree_array:
                    current_element = current_element.left
                    self.stack.append(current_element)
                    continue

                if current_element.right != None and current_element.right.data not in self.tree_array:
                    current_element = current_element.right
                    self.stack.append(current_element)
                    continue
                break


class RightLeftIterator(IIterator):
    def __init__(self, collection: TreeCollection):
        self.collection = collection
        self.stack = list()
        self.tree_array = list()
        self.current_element = -1
        self.__build_tree_array()

    def get_next(self):
        try:
            self.current_element += 1
            return self.tree_array[self.current_element]
        except IndexError:
            raise StopIteration()

    def has_more(self):
        return self.current_element < len(self.tree_array) - 1

    def __build_tree_array(self):
        current_element: TreeCollection = copy.deepcopy(self.collection)
        self.stack.append(current_element)
        self.stack.append(current_element) # Two times 'cuz there is a pop in the while
        while True:
            if len(self.stack) == 0:
                break

            current_element = self.stack.pop()

            while current_element != None:
                if current_element.data not in self.tree_array:
                    self.tree_array.append(current_element.data)

                if current_element.right != None and current_element.right.data not in self.tree_array:
                    current_element = current_element.right
                    self.stack.append(current_element)
                    continue

                if current_element.left != None and current_element.left.data not in self.tree_array:
                    current_element = current_element.left
                    self.stack.append(current_element)
                    continue
                break


if __name__ == '__main__':
    tree = TreeCollection(5)
    tree.left = TreeCollection(3)
    tree.left.left = TreeCollection(2)
    tree.left.right = TreeCollection(4)
    tree.left.left.left = TreeCollection(1)

    tree.right = TreeCollection(8)
    tree.right.right = TreeCollection(9)
    tree.right.left = TreeCollection(7)
    tree.right.left.left = TreeCollection(6)

    iterator: IIterator = tree.get_right_left_iterator()
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.has_more())
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.has_more())