# Python program for simple Python Calculator

def addition(number1, number2):
    result = number1 + number2
    print('The Result is : '+str(result))

def subtract(number1, number2):
    result = number1 - number2
    print('The Result is : '+str(result))

def multiplication(number1, number2):
    result = number1 * number2
    print('The Result is : '+str(result))

def divide(number1, number2):
    result = number1 / number2
    print('The Result is : '+str(result))                                 

print('1. Addition')
print('2. Substraction')
print('3. Mutltiplication')
print('4. Division')
print('5. Exit')

while True:
    choice = int(input('Enter Choice : '))
    if (choice >= 1 and choice  <= 4):
        print('Enter two numbers ')
        num1 =  int(input('Enter First Number : '))
        num2 = int(input('Enter Second Number : '))
        if choice == 1:
            addition(num1, num2)
        elif choice == 2:
            subtract(num1, num2)
        elif choice == 3:
            multiplication(num1, num2)
        else:
            divide(num1, num2)
    elif choice == 5:
        break
    else:
        print('You Enter wrong choice!!!')
