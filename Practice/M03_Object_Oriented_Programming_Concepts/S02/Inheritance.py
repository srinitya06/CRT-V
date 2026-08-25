'''
Inheritance: Acquring properties from one class to another class.
Types of Inheritance:
1.SINGLE
2.MULTIPLE
3. MULTILEVEL
4. HIERARCHICAL
5. HYBRID
'''

#Single Inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
b = B()
b.display1()
b.display2()

#Multilevel Inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
class C(B):
    def display3(self):
        print("This is class C display method")
c = C()
c.display1()
c.display2()
c.display3()

#Hierarchical Inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B(A):
    def display2(self):
        print("This is class B display method")
class C(A):
    def display3(self):
        print("This is class C display method")

#Multiple Inheritance
class A:
    def display1(self):
        print("This is class A display method")
class B:
    def display2(self):
        print("This is class B display method")
class C(A,B):
    def display3(self):
        print("This is class C display method")
c = C()
c.display()