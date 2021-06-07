import random
import Live


def generate_number():
   return random.randint(1, Live.difficulty)

def get_guess_from_user():
    print("you will need to choose a number to see if it matches the computer number")
    return Live.find_range(Live.difficulty)

def compare_results(secret_number,user_number):
    if user_number == secret_number:
        return True
    return False

def play():
    print(Live.difficulty)
    secret_number = generate_number()
    user_number = get_guess_from_user()
    return compare_results(secret_number,user_number)

