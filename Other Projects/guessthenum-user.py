import random

# Guess the number - user guess

def guess(x):
    random_number = random.randint(1, x)
    guessed_number = 0
    
    while(guessed_number != random_number):
        guessed_number = int(input(f"Enter a number between 1 and {x}: "))
        
        if(guessed_number < random_number):
            print("try again! too low")
        elif(guessed_number > random_number):
            print("try again! too high")
            
    print(f"yay! you got it. number is {random_number}")

guess(100)
