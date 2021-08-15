import random

def play():
    user = input("Enter Your Choice: 'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r', 's', 'p'])
    
    if user == computer:
        return "it\'s a tie."
    
    if is_win(user, computer):
        return "You Won!"
    
    
    return "You Lost!"
    

def is_win(player, oponent):
        if (player == 'r' and oponent == 's') or (player == 's' and oponent == 'p') \
        or (player == 'p' and oponent == 'r'):
            return True
            
print(play())        