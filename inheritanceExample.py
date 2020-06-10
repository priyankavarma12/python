#Inheritance Example

class Parent:
    parentAttr = 100
    def __init__(self):
        print('Calling Parent Constructor')

    def parentMethod(self):
        print('Calling Parent Method')

    def setAttr(self, attr):
        Parent.parentAttr =  attr

    def getAttr(self):
        print('Parent Attribute : ', Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print('Calling child Constructor')

    def childMethod(self):
        print('Calling Child Method')


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(300)
c.getAttr()

    
