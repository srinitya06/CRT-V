'''Polymorphism:
poly ==> many 
morph ==> forms
1.commpile-time
   1. Function Overloading - Creating multiple functions with same name 
   and different argumrnt lists
   2. Operator Overloading 
2. Run-Time 
   1. Method Overriding
'''
# function overloding:
'''
def add(a,b):
    return a+b 
def add(a,b,c):
    return a+b+c 
def add(a,b,c,d):
    return a+b+c+d 
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
'''

'''python does not support function overloading directly.
we can acheive this using variable-length arguments(using * ).'''
def add(*values):
    return sum(values)
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))

#Opeator overloading
class A:
    def __init__(self,x):
        self.x = x 
    def __add__(self,val):
        return self.x + val.x
    def __lt__(self,val):
        return self.x < val.x
    def __sub__(self,val):
        return self.x - val.x
a = A(10)
b = A(20)
print(a+b)
print(a-b)
print(a<b)

#Example 
class B:
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    def __add__(self,val):
        return (self.x + val.x, self.y + val.y)
    def __sub__(self,val):
        return (self.x - val.x, self.y - val.y)
a = B(10, 20)
b = B(30, 40)
print(a + b)
print(a - b)

# Method Overriding: Same method in both parent and child class 
class Parent:
    def display(self):
        print("Parent class display method")
class Child(Parent):
    def display(self):
        print("child class display method")
c = Child()
c.display() #Child class method
Parent.display(c) # Parent class method

#Duck typing 
class Dog:
    def Sounds(self):
        print("Bark")
class Cat:
    def Sounds(self):
        print("Meow")
def make_sound(animal):
    animal.Sounds()
d = Dog()
c = Cat()
make_sound(d)
make_sound(c)
