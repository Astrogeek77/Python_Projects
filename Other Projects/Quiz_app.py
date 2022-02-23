print("Welcome to my quiz, Answer 10 simple questions to be the boss")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Ques 1
answer = input("When was python first released? ")
if answer.lower() == "1991":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ques 2
answer = input("When was javascript first released? ")
if answer.lower() == "1995":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ques 3
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ques 4
answer = input("Total number of islands comprising philipines?")
if answer.lower() == "7640":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ques 5
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# Ques 1
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
