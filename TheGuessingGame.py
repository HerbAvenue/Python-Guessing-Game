from random import Random, randint

keep_playing = input("Welcome to The Guessing Game! Do you want to play? ")

def play_game():

    difficulty = input("Enter a difficulty. 1 = Easy, 2 = Medium, 3 = Hard: ")
    
    #ENSURES THE DIFFICULTY PICKED IS VALID
    difficulties = {'1': 'easy', '2': 'medium', '3': 'hard'}
    while difficulty not in difficulties:
        difficulty = input("This is not a difficulty! Please enter 1 = Easy, 2 = Medium, or 3 = Hard: ")
    else:
        print("Nice! You have chosen the " + difficulties[difficulty] + " difficulty!")

    num_range = []
    if difficulty == '1':
        num_range = list(range(1, 11))
        #print(num_range)

    elif difficulty == '2':
        num_range = list(range(1, 51))
        #print(num_range)

    elif difficulty == '3':
        num_range = list(range(1, 101))
        #print(num_range)

    
    correct_answer = num_range[randint(1, len(num_range))]

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
        print("The correct answer was", correct_answer)

    else:
        print("Yay! You did it! (Wait, really? How?)")

        

while keep_playing.upper() == "YES":
    play_game()
    keep_playing = input("Keep playing? ")
else:
    exit



