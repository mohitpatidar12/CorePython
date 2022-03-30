from Shape import *
r=int(input("enter radius = "))
class Circle (Shape):
    PI=3.14
    def __init__(self,r,c="",b=0):
        self.__radius =r
        super(Circle, self).__init__(c, b)

    def area(self):
            return self.__radius * self.__radius * Circle.PI