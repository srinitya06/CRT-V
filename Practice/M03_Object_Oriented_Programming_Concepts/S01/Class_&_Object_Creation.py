class Example:
    x = 100 
    def display(self):      
        print("This is an example of a class method.")
obj = Example()
obj.display()
print(obj.x)

#class circle with area and perimeter methods
from math import pi 
class Circle:
    r = 7 
    def Area(self):
        return pi * self.r * self.r
    def Perimeter(self):
        return 2 * pi * self.r

c = Circle()
print(c.Area())
print(c.Perimeter())