import random
import time

# global variables
odd = 50 * '-'
game_stats = list()

def main():

    # Sets the basic parameters for the game set, part of them by dialogue with player
    digits, zero = settings()
    guesses = 0
    games = 0

    # Communication with player - "do you want to play (again), or to quit the program?"
    # In case decision is to quit, function play_or_not exits the program
    # In case decision is to play, the code continues running
    # Change in settings is not possible (if player wanted to play with 4 digits, he plays alike in a whole set, etc.)
    while True:
        play_or_not(games)
        games += 1
        numb_to_guess = get_number(digits, zero)
        start_time = time.time()

    # The single game
        while True:
            guesses += 1
            actual_guess = guess(digits)
            bulls, cows = bulls_cows(numb_to_guess, actual_guess)
            print('{} |Bulls: {} |Cows: {} |Attempts: {}'.format(actual_guess, bulls, cows, guesses))
            if bulls == digits:
                game_time = time.time() - start_time
                print('Congratulations! You have guessed the number!')
                print(odd)
                create_stats(games, numb_to_guess, guesses, game_time)
                guesses = 0
                break

def settings() -> tuple:
    '''Asks the player for basic game settings'''

    print('''Hello, player! You are starting with a popular game BULLS AND COWS!
Now we can choose the game options''')
    print(odd)

    print('''At first, please choose the number of digits you will play with
It can be from 3 to 5''')
    digits = int(input('Number of digits: '))
    print(odd)

    print('''Second thing - do you want to allow zero to be a possible first digit? 
If you want to allow zero in the first digit position, insert "z"
Otherwise insert "n"''')

    while True:
        zero_choice = input('Your decision regarding zero as possible first digit: ')
        if zero_choice.lower() == 'z':
            zero = True
            break
        elif zero_choice.lower() == 'n':
            zero = False
            break
        else:
            print('Incorrect choice. Read instructions and try again!')
            print(odd)

    return digits, zero

def get_number(digits: int, zero_beg = False) -> str:
    '''Returns a random number which will be guessed by the player'''

    numb_lst = random.sample(range(10), digits)
    if zero_beg == False:
        while numb_lst[0] == 0:
            numb_lst = random.sample(range(10), digits)

    return "".join([str(i) for i in numb_lst])

def guess(digits: int) -> str:
    '''Returns a single guess from the player
Contains a control of the right amount of digits
The amount of digits must be acc. to basic settings from communication()'''

    while True:
        print(odd)
        numb = input(f'Guess a {digits} digit number: ')
        if not numb.isdigit():
            print('Your guess is not a digit! Try again!')
        elif len(numb) != digits:
            print('Wrong amount of digits! Try again!')
        else:
            break

    return numb

def bulls_cows(numb1: str, numb2: str) -> tuple:
    '''Compares 2 lists of numbers.
Returns overall amount of bulls and cows from the comparison.'''
    bulls = 0
    cows = 0

    for i in range(len(numb1)):
        if numb1[i] == numb2[i]:
            bulls += 1
        elif numb1[i] in numb2:
            cows += 1

    return bulls, cows

def play_or_not(games: int):
    '''Leads a dialogue with the player.
Possible decisions are to continue playing or to stop playing.
If player wants to stop playing, program is stopped and game statistic is printed.
If player wishes to play, code continues and new game is started.'''

    print(odd)
    if games == 0:
        print('Do you want to play the first game?')
    else:
        print('Do you want to play again?')

    print('If yes, choose p')
    print('If no, choose q')

    while True:
        decision = input('Enter your decision regarding playing: ')

        if decision.lower() == 'q':
            print(odd)
            if games == 0:
                print('Game statistics:')
                print('0 games were played')
                print('No data to do game statistics')
                print('Play at least 1 game next!')
                exit()
            else:
                print('Game statistics:')
                print_stats()
                print(odd)
                print('See you later!')
                exit()

        elif decision.lower() == 'p':
            print(odd)
            break

        else:
            print('Your choice is not valid. Read instructions and try again!')
            print(odd)

def formatted_time (t: float) -> str:
    '''Converts time into format mm:ss'''

    m, s = divmod(int(t), 60)
    return f'{m:0>2}:{s:0>2}'

def create_stats(g: int, n: str, a: int, t: float) -> None:
    '''Appends the statistic of the played game into global variable game_stats
After the last game of the set, the variable game_stats contains statistic of all played games'''

    stats_dict = dict(game=g, number=n, attempts=a, time=formatted_time(t))
    game_stats.append(stats_dict)

def print_stats() -> None:
    '''Prints the overall statistic from the game set when player decides to quit playing'''

    print('| {} | {} | {} | {} |'.format('Game', 'Guessed number', 'Attempts', 'Time (mm:ss)'))
    for record in game_stats:
        print('| {game:^4} | {number:^14} | {attempts:^8} | {time:^12.5} |'.format(**record))

main()
