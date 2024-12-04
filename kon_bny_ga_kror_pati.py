question=[
"what is the capital of pakistan?",
"what is the capital of turky?",
"what is the capital of usa?",
"what is the capital of india?"
]
answer=[
"islamabad",
"istanbul",
"california",
"dheli"
]
question2=[
"Fasil masjid is where located?",
"Badsahi masjid is where located?",
"perth city is where located?",
"what is short form of united kingdome?"
]
answer2=[
"islamabad",
"Lahore",
"austrlia",
"uk"
]
levels=[
1000,
2000,
3000,
4000,
5000,
6000,
7000,
8000,
9000
]
for i in range(0,len(question)):
    print(f"question {i+1}\n{question[i]}")
    user=input("enter your ans: ")
    if user.lower().strip()==answer[i]:
        print("correct ans")
        print(f"your amount is {levels[i]}")
    else:
        print("wrong")
        print(answer[i])
        print(f"your amount is {levels[i-1]}")

if len(question)==4:
        for j in range(0,len(question2)):

            print(f"part 2\n question {j+1}\n {question2[j]}")
            user2=input("enter your ans: ")
            if user2.lower().strip()==answer2[j]:
                print("correct")
                print(levels[i])
            else:
                print("wrong")
                print(answer2[j])