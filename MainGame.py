import Live
import Score

print(Live.welcome("guy"))
if Live.load_game() == False:
    print("Sorry you have lost the game ):")
else:
    Score.add_score(Live.difficulty)
    print("Congratulations you have Won!!!!")
