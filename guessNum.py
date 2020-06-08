import random

def guess_num():
    global guess
    for i in range(1,4):
        print('Try to guess the Number ')
        guess = int(input('Enter Number between 1 and 20 : '))

        if guess < secretNumber:
            print('The Number you specified is Too Low')
        elif guess > secretNumber:
            print('The Number you specified is Too High')
        else:
            break
def check(guess, secretNumber):
    if guess == secretNumber:
        print('Congratulations! You have guessed the number!!')
    else:
        print('Better Luck next time! The correct Number was '+str(secretNumber))
        
secretNumber = random.randint(1,20)
print('I am currently thinking of a number !')

guess_num()
check(guess, secretNumber)


    
