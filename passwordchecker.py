password = 'password123'

input_password = input('Please enter the password : ')

input_password = str(input_password)

if input_password  == password:
    print('Correct Password! ')
    print('Access granted! ')
else:
    print('Wrong password')
    print('Access denied! ')
    
    
