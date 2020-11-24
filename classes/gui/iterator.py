from abc import ABCMeta, abstractstaticmethod

class iIterator(metaclass=ABCMeta):
    @abstractstaticmethod
    def has_next():
        """Returns Boolean wheather as end of collection or not"""

    @abstractstaticmethod
    def next():
        """ Returns the object in the collection """

class Iterable(iIterator):
    def __init__(self):
        self.index = 0
        self.maximum = 9

    def next(self):
        if self.index < self.maximum:
            x = self.index
            self.index += 1
            return x
        else:
            raise Exception("AtEndOfIteratorException", "At the end of Iterator")
    
    def has_next(self):
        return self.index < self.maximum