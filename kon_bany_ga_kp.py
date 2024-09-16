import time
from sty import fg,ef,rs

score=0
try:
    name=input(f"{fg.black}Insert Your Name: {fg.rs}")
    age=int(input(f"{fg.black}Enter Your Age : {fg.rs}"))
    print(f"{fg.yellow}______WellCome {name} to KBC{fg.rs}")
    if age>=18:
        print(f"{fg.green}Loding...{fg.rs}")
        time.sleep(3)
        print(f"{fg.yellow}___Let's Play a Game____{fg.rs}")
    else:
        print(f"{fg.green}Loding...{fg.rs}")
        time.sleep(3)
        print(f"{fg.red}You Can't Play It{fg.rs}")
        quit()
except ValueError:
    print(f"{fg.green}Loading...{fg.rs}")
    time.sleep(3)
    print(f"{fg.red}Sorry{fg.rs}")

question=[
"fasil masjid is where located?",
"peramid is where located?",
"what is stand for ram?",
"waht is the name of best hacker?",
"who was the strongest prim minster of iran?"

]
# ans
answers=[
"islamabad",
"egypt",
"random access memory",
"hamza",
"sadam hussain"

]

# part 2
quetions2=[
"minare pakistan is where?",
"what is name of jani?",
"what is the name of jani's jani?",
"what is the name of little bro?",
"what are you doing?"

]
# part2 ans
ans2=[
"lahore",
"qasim",
"father and mother",
"qasim",
"nothing"

]
question_score=0
# ans=input("enter your ans: ")
amount=[
"1000",
"2000",
"4000",
"6000",
"7000",
"8000",
"9000",
"10000"
]
# for k in range(len(amount)):
    
while True:
    try:
        # for k in range(len(amount)):
            for i in range(len(question)):
                print(f"{fg.green}Loding...{fg.rs}")
                time.sleep(3)
                print(f"{fg.blue}Q:{i+1} {question[i]}")
                user_input=input(f"{fg.black}Enter Your Answer and type Q for (quit): {fg.rs}")
                if user_input.isalpha:
                    user_input=str(user_input)
                    if user_input.lower().strip()=="q":
                        print(f"{fg.green}Loding...{fg.rs}")
                        time.sleep(3)
                        print(f"{fg.yellow}Done!{fg.rs}")
                        quit()

                        
                    elif user_input.lower().strip()==answers[i]:
                        print(f"{fg.green}Loding...{fg.rs}")
                        time.sleep(3)
                        b=print(f"{fg.green}____Correct___{fg.rs}")
                        print(b)
                        question_score+=1
                            
                        # print(f"{fg.yellow}you got money {k}")
                        print(f"{fg.yellow}{question_score}{fg.rs}")
                            
                            
                        if question_score>=4:
                            for j in range(len(quetions2)):
                                print(f"{fg.blue}Q:{j+1} {quetions2[j]}")
                                user_input=input(f"{fg.black}Enter Your Answer and type Q for (quit): {fg.rs}")
                                if user_input.lower().strip()=="q":
                                    quit()
                                elif user_input.lower().strip()==ans2[j]:
                                    print(f"{fg.green}Loding...{fg.rs}")
                                    time.sleep(3)
                                    print(f"{fg.green}___Correct___{fg.rs}")
                                    # print(f"{fg.yellow}you got money {amount[k]}")
                                else:
                                    print(f"{fg.green}Loding...{fg.rs}")
                                    time.sleep(3)
                                    print(f"{fg.red}InCorrect\nthe correct ans is {ans2[j]}{fg.rs}")
                    else:
                        print(f"{fg.green}Loding...{fg.rs}")
                        time.sleep(3)
                        print(f"{fg.red}InCorrect\nthe correct ans is {answers[i]}{fg.rs}")
    except ValueError:
        print(f"{fg.red}Error{fg.rs}")                        
