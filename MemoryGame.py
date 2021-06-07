import random
import time
import os
import Live


def generate_sequence():
    random_list = []
    for i in range(0, Live.difficulty):
        n = random.randint(1, 101)
        random_list.append(n)
    return random_list

def get_list_from_user():
    number_list = []
    print("\n")
    print("let check if you remembered the sequence\n ")
    for i in range(0, Live.difficulty):
        print("Enter number at index", i, )
        item = int(input())
        number_list.append(item)
    return number_list


def is_list_equal(random_list,number_list):
   random_list.sort()
   number_list.sort()
   if random_list == number_list:
       return True
   return False

def print_list(list):
    print(*list, sep=", ")


def clear():
    for x in range(100):
        print()

def play():
    print(Live.difficulty)
    random_list = generate_sequence()
    print_list(random_list)
    time.sleep(0.7)
    clear()
    number_list = get_list_from_user()
    return is_list_equal(random_list,number_list)

