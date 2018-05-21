import random
num= random.randint(1,100)
while True:
    print('guess a number 1 through 100 ')
    guess=input()
    i = int(guess)
    if i == num:
        print("You guessed it!")
        break 
    elif i < num:
        print("some more") 
    elif i > num:
        print("less")  
