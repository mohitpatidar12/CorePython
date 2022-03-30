from abc import ABC ,abstractmethod
class  Shape(ABC):
    def __init__(self,c,b):
        self.color= c
        self.borderWidth =b
    @abstractmethod
    def area(self):
        pass
    def getcolor(self):
        return self.color

    def getBorderWidth(self):
         self.borderWidth=0

    def __str__(self):
        return self.color