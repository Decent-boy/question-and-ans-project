
# question Quiz game
import time
print("wellom to qiz game ")
def playing_game(playing):
    try:
        if playing.lower()=="yes":
            print("working...")
            time.sleep(5)
            print("Done!")
            print("let's get statrted...")
            
        elif playing.lower()=="no":
            print("it's working...")
            time.sleep(7)
            print("Done!")
            quit()
            
        else:
            print("invalid")
            quit()
    except ValueError:
        print("invalid")
def questions(ask_questions,correct,score):
    question=input(ask_questions)
    if question.lower()==correct:
        print("correct")
        score+=1
    else:
        print("uncorrect")
    return score
playing=input("do you want to play yes or not : ")
playing_game(playing)
# score 
score=0
# call fun
score=questions("what is short form centeral processing unit\n : ","cpu",score)
score=questions("what is short form randome access memory\n : ","ram",score)
score=questions("what is short form graphic processing unit\n : ","gpu",score)
score=questions("what is the brain of computer\n : ","cpu",score)
print(f"your total question was corrected {score}")
print(f"your score and averge is  {(score/4)*100} %")
if (score/4)*100>50:
    print("congurlation")
