#python program for exception

def divide_byZero_error():
    try:
        a = 3
        b = 0
        c = a/b
        print(c)
    except ZeroDivisionError:
        print('Can\'t Divide by Zero !')
    else:
       print('Invalid inputs')

def ioexception():
    try:
        fn = open('addfe')
        fn.write('This is a test file')
    except IOError:
        print('Cant open that file, It doesnt exist !!!')
    else:
        print('Everything Worked Well!')
         
divide_byZero_error()
ioexception()   
    
    
