import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    if player not in choices:
        player = input('rock, paper or scissors: ').lower()

    print('computer: ', computer)
    print('player: ', player)

    if player == computer:
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer win!')
        if computer == 'scissors':
            print('Player win!')
    elif player == 'paper':
        if computer == 'scissors':
            print('Computer win!')
        if computer == 'rock':
            print('Player win!')
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer win!')
        if computer == 'paper':
            print('Player win!')
            
    play_again = input('wanna play again? (yes/no): ').lower()
    if play_again == 'no':
        break

print('bye!')

