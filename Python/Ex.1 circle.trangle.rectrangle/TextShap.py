from textcircle  import *
from textTriangle import *
from textRectangle import *

tri_obj = Triangle(base,height)
c= tri_obj.area()

rec_obj = Rectangle(length,width)
a= rec_obj.area()

cir_obj = Circle(r)
b= cir_obj.area()

print( "arrey of value triagle : " ,tri_obj.area())
print("arrey of value Rectangle :",rec_obj.area())
print("arrey of circle :",cir_obj.area())