from sty import fg
import time
print(f"{fg.blue}_________WellCome To Quiz Game________{fg.rs}")
name=input(F"{fg.blue}Insert Your Name: {fg.rs}")
age=int(input(f"{fg.blue}Enter Your Age: {fg.rs}"))
if age>=18:
    print(f"{fg.green}Loding...{fg.rs}")
    time.sleep(3)
    print(f"{fg.blue}____________Let's Get Started {name}_________{fg.rs}")
else:
    print(f"{fg.green}Loding...{fg.rs}")
    time.sleep(3)
    print(f"{fg.blue}......Done.....{fg.rs}")
score=0
def quizgame():
    global score
part_1=[
" What is the Capital of Pakistan?",  
" Pyramid is located where?",  
" What does RAM stand for?",  
" What is the name of the best hacker?",  
" How many rukans in Islam?"

]
ans_part_1=[
"islamabad",  
"egypt",  
"random access memory",  
"hamza",  
"five"

]
# part 2 questions
part_2=[
"Q1: Who is known as the father of computer science?",  
"Q2: What is the largest planet in our solar system?",  
"Q3: What is the chemical symbol for gold?",  
"Q4: Who wrote 'Romeo and Juliet'?",  
"Q5: What is the powerhouse of the cell?" 

]
ans_part_2=[
"alan turing",  
"jupiter",  
"au",  
"william shakespeare",  
"mitochondria"

]
user_play=input(f"{fg.blue}Are you wanted to play type (y/n(Yes/Not)){fg.rs}")
if user_play.strip().lower()=="y":
    print(f"{fg.green}Loding...{fg.rs}")
    time.sleep(3)
    print(f"{fg.blue}_____....____WellCome Again___....___{fg.rs}")
else:
    print(f"{fg.green}Loding...{fg.rs}")
    time.sleep(3)
    
    # 2nd func
def play_quiz(part_1,ans_part_1):
    global score
    for i in range(len(part_1)):
        user_input=input(f"{fg.red}Q:{i+1}=={part_1[i]}{fg.rs} \n: ")
        if user_input.strip().lower()==ans_part_1[i]:
            print(f"{fg.green}Loding...{fg.rs}")
            time.sleep(3)
            print(f"{fg.blue}______Correct_______{fg.rs}")
            score+=1
        else:
            print(f"{fg.green}Loding...{fg.rs}")
            time.sleep(3)
            print(f"{fg.blue}______InCorrect_______\nThe Correct answer is {ans_part_1[i]}{fg.rs}")
        print(f"{fg.green}You Got Right Anss are {score} {fg.rs}")
        print(f"{fg.green}Your avrage score is {(score*(len(part_1))/100)}%")

play_quiz(part_1,ans_part_1)
    # function part 2 for part 2 questions
def Quiz_part_2(part_2,ans_part_2):
    global score
    if score==4:
        print(f"{fg.blue}__OO__You can play a part 2___OO__{fg.rs}")
        for i in range(len(part_2)):
            user_input_p2=input(f"{fg.red}Q:{i+1}=={part_2[i]}\n: ")
            if user_input_p2.strip().lower()==ans_part_2[i]:
                print(f"{fg.green}Loding...{fg.rs}")
                time.sleep(3)
                print(f"{fg.blue}_____Correct____{fg.rs}")
                score+=1
            else:
                print(f"{fg.green}Loding...{fg.rs}")
                time.sleep(3)
                print(f"{fg.blue}_____InCorrect____\nThe Correct ans is {ans_part_2[i]}{fg.rs}")
            print(f"{fg.blue}Thank you for playing {fg.rs}")
            print(f"{fg.green}You got score {score}{fg.rs}")
            print(f"{fg.green}your avrage score is{(score*(len(part_2))/100)}%")
Quiz_part_2(part_2,ans_part_2)
        




"""import time  
from sty import fg, bg, rs  

# Function of game  
print(f"{fg.blue}__________Welcome To Quiz Game__________{fg.rs}")  
scor = 0  

def Quizgame():  
    global scor  

    name = input("Insert your Name: ")  
    age = int(input("Enter Your Age: "))  
    if age >= 18:  
        print(f"{fg.green}Loading...{fg.rs}")  
        time.sleep(3)  
        print(f"{fg.blue}Let's Get Started {name}_____{fg.rs}")  
    else:  
        print(f"{fg.red}Sorry, you must be at least 18 to play.{fg.rs}")  
        return  

    # Part 1 Questions  
    questions_part_1 = [  
        "Q1: What is the Capital of Pakistan?",  
        "Q2: Pyramid is located where?",  
        "Q3: What does RAM stand for?",  
        "Q4: What is the name of the best hacker?",  
        "Q5: How many rukans in Islam?"  
    ]  
    answers_part_1 = [  
        "islamabad",  
        "egypt",  
        "random access memory",  
        "hamza",  
        "five"  
    ]  
    
    # Play Part 1  
    play_quiz(questions_part_1, answers_part_1)  

    # Part 2 Questions  
    questions_part_2 = [  
        "Q1: Who is known as the father of computer science?",  
        "Q2: What is the largest planet in our solar system?",  
        "Q3: What is the chemical symbol for gold?",  
        "Q4: Who wrote 'Romeo and Juliet'?",  
        "Q5: What is the powerhouse of the cell?"  
    ]  
    answers_part_2 = [  
        "alan turing",  
        "jupiter",  
        "au",  
        "william shakespeare",  
        "mitochondria"  
    ]  

    # Ask if user wants to play part 2  
    should_play_part_2 = input("Do you want to play Part 2? (yes/no): ")  
    if should_play_part_2.strip().lower() == "yes":  
        play_quiz(questions_part_2, answers_part_2)  
    else:  
        print(f"{fg.green}Thank you for playing! Your final score is {scor}.{fg.rs}")  

def play_quiz(questions, answers):  
    global scor  
    for i in range(len(questions)):  
        user_ans = input(f"{fg.red}{questions[i]} {fg.rs}")  
        if user_ans.lower() == answers[i]:  
            print(f"{fg.green}Loading...{fg.rs}")  
            time.sleep(3)  
            print(f"{fg.blue}______Correct_____{fg.rs}")  
            scor += 1  
        else:  
            print(f"{fg.green}Loading...{fg.rs}")  
            time.sleep(3)  
            print(f"{fg.blue}_____Incorrect______{fg.rs}")  
            print(f"{fg.li_green}The Correct answer is {answers[i]}{fg.rs}")  
        
        print(f"{fg.li_green}You have a score of {scor}:{fg.rs}")  
        print(f"{fg.li_green}Your score percentage is {(scor / len(questions) * 100):.2f}%{fg.rs}")  

Quizgame()"""