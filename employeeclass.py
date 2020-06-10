class Employee:
        empCount = 0
        def __init__(self, name, email, age):
            self.name =  name
            self.email = email
            self.age = age
            Employee.empCount += 1

        def displayCount(self):
            print('Total Employee Number is : '+ str(Employee.empCount))

        def displayInformation(self):
            print('Name : ', self.name, 'Email: ', self.email, 'Age: ', self.age)

employee1 = Employee('Adam', 'adam@gmail.com', '20')
employee1.displayInformation()
employee1.displayCount()

employee2 = Employee('Jack','jack@gmail.com','21')
employee2.displayInformation()

print('There are '+ str(Employee.empCount) + ' employee in the company.')

print('There are %d employee in the company.' % (Employee.empCount))

print('Age of employee is %d ' %(int(employee1.age)))

print('Employee 2 age is '+ getattr(employee2, 'age'))

print('Attribute exist or not ' + str(hasattr(employee1, 'phonenumber')))

print('Employee 1 name is '+ getattr(employee1, 'name'))

employee1.displayInformation()

setattr(employee1, 'name', 'Adams')
