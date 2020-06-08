input_string = input('Enter the string you want ::')

def reverse_string(input_string):
    print(input_string[::-1])
   
reverse_string(input_string)

def even_odd(number):
    if (number % 2 == 0):
        print('The Number is Even ')
    else:
        print('The Number is Odd ')

input_number = int(input('Enter the number you want : '))
even_odd(input_number)
