import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 404

def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')
