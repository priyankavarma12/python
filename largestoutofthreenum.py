# Python program - Find the largest out of three numbers

def check_for_largest(num1,num2,num3):
    global largest
    largest = num1
    if largest < num2:
        if num2 > num3:
            largest = num2
        else:
            largest = num3
    elif largest < num3:
        if num3 > num2:
            largest = num3
        else:
            largest = num2
    else:
        largest = num1
    return largest

count = 1
print('Enter x to exit the program. ')
print('Enter three numbers ')

num1 = int(input('Enter the First number : '))
if num1 == 'x':
    exit()
else:
    num1 = int(num1)
    num2 = int(input('Enter the Second number : '))
    num3 = int(input('Enter the Third number : '))
    check_for_largest(num1, num2, num3)
    if num1 == num2 and num1 == num3:
        count = 0
    if count == 0:
        print('All Three numbers are equal to each other. ')
    else:
        print('Largest of The given numbers is : '+str(largest))
