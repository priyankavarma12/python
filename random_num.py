import random

def getNumber(num):
    if num == 1:
        return 'The Number is 1'
    elif num == 2:
        return 'The Number is 2'
    elif num == 3:
        return 'The Number is 3'
    elif num == 4:
        return 'The Number is 4'
    elif num == 5:
        return 'The Number is 5'

random_num = random.randint(1,5)
pick = getNumber(random_num)
print(pick)

    
