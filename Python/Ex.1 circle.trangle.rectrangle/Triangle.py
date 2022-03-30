from Shape import *
base=int(input("inter your base = "))
height=int(input("inter your height = "))
class Triangle(Shape):
  def __init__(self,base,height, c="",b=0):
      self.__base=base
      self.__height=height
      super(Triangle,self).__init__(c,b)
  def area(self):
      return (self.__base * self.__height)/2