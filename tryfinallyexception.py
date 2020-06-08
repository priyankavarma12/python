#Python Program- Try with Finally

def try_finally():

    try:
        f = open('testfile', 'w')
        f.write('This is my test file')
    finally:
        print('Cant open or find that file')
        f.close()

def convert(var):
    try:
        print(int(var))
    except ValueError as Argument:
        print("The Argument does not contain numbers \n", Argument)

convert('www')

try_finally()

