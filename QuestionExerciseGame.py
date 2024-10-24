
from Question import Question

questions_prompt = [
    "What is the color of apple?\n(a).PINK\n(b).BLUE\n(c).RED",
    "What is the shape of earth?\n(a).CIRCLE\n(b).FLAT\n(c).TRIANGLE",
    "Where is the WHITE HOUSE located?\n(a).NY\n(b).DC\n(c).FLORIDA",
]

questions = [
    Question(questions_prompt[0],"c"),
    Question(questions_prompt[1], "a"),
    Question(questions_prompt[2], "b"),
]

def run_rest(questions):
    score = 0 #every time user correct the answer, score increment
    i = 0
    for ques in questions:
        print(questions_prompt[i])
        answer = input("Type the answer: ")
        if(answer == ques.answer):
            score +=1
        i+=1
    print("You got " + str(score) + " Correct !")

run_rest(questions)