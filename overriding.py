# Python Program for overriding a methods

class Parent:
    def myMethod(self):
            print('Calling Parent Method')

class Child(Parent):
    def myMethod(self):
            print('Calling Child Method')


c = Child()
c.myMethod()

class Vector:
    def __init__(self, a, b):
            self.a = a
            self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a , self.b + other.b)


v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)
