import random

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

    
    