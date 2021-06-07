import Utils
import os

def add_score(difficulty):
    new_score = (difficulty *3) + 5
    if not os.path.exists(Utils.SCORES_FILE_NAME):
        f = open(Utils.SCORES_FILE_NAME,'w+')
        f.write(str(new_score))
    else:
        try:
            f= open(Utils.SCORES_FILE_NAME,'r+')
            score = int(f.read()) + new_score
            f.seek(0)
            f.truncate()
            f.write(str(score))
        except:
            print("can't append to file")
