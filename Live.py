import MemoryGame
import CurrencyRouletteGame
import GuessGame
difficulty = 0

def load_game():
    global difficulty
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game_type = find_range(3,False)
    difficulty = find_range(5,True)

    if game_type == 1:
        return MemoryGame.play()
    if game_type == 2:
        return GuessGame.play()
    if game_type == 3:
        return CurrencyRouletteGame.play()

def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.\n")

def find_range(max_value,diffculty = False):
    while True:
        try:
            if diffculty == True:
                intTarget = int(input(f"Please choose a difficulty between from 1 to {max_value} :"))
            else:
                intTarget = int(input(f"Please choose a number between from 1 to {max_value} :"))
        except ValueError:
            continue
        else:
            if intTarget < 1 or intTarget > max_value:
                continue
            else:
                return (intTarget)
