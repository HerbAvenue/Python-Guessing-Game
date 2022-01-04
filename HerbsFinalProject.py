from random import Random, randint

#GETS A USERS INPUT AND DESIRED DIFFICULTY
print("Welcome to the show kid.")
difficulty = input("Difficulty (1 = easy, 2, medium, 3 = hard): ")

#ENSURES THE DIFFICULTY PICKED IS VALID
difficulties = {'1': 'easy', '2': 'medium', '3': 'hard'}
while difficulty not in difficulties:
    difficulty = input("This is not a difficulty, please enter (1 = easy, 2, medium, 3 = hard): ")
else:
    print("Nice! You have chosen the " + difficulties[difficulty] + " Difficulty")




#CREATES A RANGE BASED ON CHOSEN DIFFICULTY
num_range = []
if difficulty == '1':
    num_range = list(range(0, 11))
    #print(num_range)

elif difficulty == '2':
    num_range = list(range(0, 51))
    #print(num_range)

elif difficulty == '3':
    num_range = list(range(0, 101))
    #print(num_range)


#COMPUTER SELECTS A CORRECT ANSWER
correct_answer = num_range[randint(1, len(num_range))]
#print(correct_answer)



#USER USES THEIR ATTEMPTS TO PICK THE CORRECT ANSWER
attempts = 1
user_guess = ""

print("You have 3 attempts to guess the correct number from", num_range[0], "to", num_range[-1])

while attempts == 1 and user_guess != str(correct_answer):
    print("Attempt:", attempts)
    attempts += 1
    user_guess = input("What is your guess? ")

while attempts > 1 and attempts < 4 and user_guess != str(correct_answer):
    print("Attempt:", attempts)
    attempts += 1
    print("Try again!")
    user_guess = input("What is your guess? ")

if attempts >= 4 and user_guess != str(correct_answer):
    print("You're not smart enough for this!")

else:
    print("Yay! You did it! (Wait, really? How?)")









