import random

# Guess the number - user guess

# def guess(x):
#     random_number = random.randint(1, x)
#     guessed_number = 0
    
#     while(guessed_number != random_number):
#         guessed_number = int(input(f"Enter a number between 1 and {x}: "))
        
#         if(guessed_number < random_number):
#             print("try again! too low")
#         elif(guessed_number > random_number):
#             print("try again! too high")
            
#     print(f"yay! you got it. number is {random_number}")

# guess(100)



# Guess the number - computer guess


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while(feedback != 'c'):
        if high != low:
            guessed_number = random.randint(low, high)
        else:
            guessed_number = low
            
        feedback = input(f"Is {guessed_number} too high(H) or too low(L) or correct(C)?? ").lower()
        
        if feedback == 'h':
            high = guessed_number - 1
        elif feedback == 'l':
            low = guessed_number + 1
    
    print(f"yay! the computer guessed your number {guessed_number}, correctly!")

computer_guess(1000)

    
    