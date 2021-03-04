import random

UPPER_BOUND = 25
highscore = (None, None)

def start_game(score_prompt=''):
    print(score_prompt or "Let's play a number guessing game!\n")
    player_name = input('What is your name?:    ')
    print(f'Welcome, {player_name}!\n')
    print(f'I am thinking of a number between 1 and {UPPER_BOUND}, inclusive.')
    play_game(player_name)
    play_again()

def play_game(player):
    solution = random.randint(1, UPPER_BOUND)
    counter = 0
    while True:
        try:
            counter += 1
            guess = int(input('Can you guess my number?:    '))
            if handle_guess(solution, guess) == True:
                handle_score(player, counter)
                break
        except ValueError as err:
            counter -= 1
            handle_error(err)

def handle_guess(correct_answer, player_input):
    if player_input < 1 or player_input > UPPER_BOUND:
        raise ValueError(f'Number must be between 1 and {UPPER_BOUND}.')
    elif correct_answer == player_input:
        return True
    elif correct_answer < player_input:
        print(f"It's lower than {player_input}.\n")
    elif correct_answer > player_input:
        print(f"It's higher than {player_input}.\n")

def handle_error(error):
    if 'invalid literal' in str(error):
        print('Please enter a positive whole number.\n')
    else:
        print(error, '\n')

def handle_score(name, score):
    print(f'Nice, {name}! You got it in {score} guesses!')
    global highscore
    if highscore == (None, None) or score < highscore[1]:
        print('You set a new High Score!\n')
        highscore = (name, score)
    elif score == highscore[1]:
        print(f"You tied {highscore[0]}'s score and took their spot!\n")
        highscore = (name, score)
    else:
        print(f"You did not beat {highscore[0]}'s score :(\n")

def play_again():
    answer = input('Enter Y to play again, or any other key to exit:    ')
    if answer.lower() == 'y':
        prompt = f"Let's play again! The High Score is {highscore[1]} by {highscore[0]}.\n"
        start_game(prompt)
    else:
        print('Thanks for playing!')

start_game()