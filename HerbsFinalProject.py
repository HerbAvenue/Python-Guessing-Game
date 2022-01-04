from random import Random, randint

#GETS A USERS INPUT AND DESIRED DIFFICULTY
name = input('What is your name? ')
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
correct_answer = num_range[randint(0, len(num_range))]



#USER USES THEIR ATTEMPTS TO PICK THE CORRECT ANSWER
attempts = 1
print("You have 3 attempts to guess the correct number from", num_range[0], "to", num_range[-1])

while attempts < 4:
    print("Attempt:", attempts)
    guess = input("What is your guess? ")

    if guess == str(correct_answer):
        print("You got it!")
        break

    else:
        print("Try again")
        attempts += 1


print("You're a fucking loser")
   






