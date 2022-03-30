from Shape import *
length = int(input("inter your length = "))
width = int(input("enter your width = "))
class Rectangle(Shape):
   def __init__(self,length,width, c='',b=0):
      self.__length=length
      self.__width=width
      super(Rectangle,self).__init__(c,b)

   def area(self):
        return self.__length * self.__width