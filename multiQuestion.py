import pyttsx3
from Question import Question
from datetime import datetime
import time
from time import *
engine = pyttsx3.init()
# Array of questions to ask players
question_prompt = [
    "Where is Lambogini made? (a) Germany\n (b) Italy\n (c) Nigeria\n\n",
    "Who is the first man to travel to space? (a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n",
    "Who is the first man to land on the moon? (a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n",
    "Who is the founder of Apple Inc.? (a) Mark Zuckerberg\n (b) Steve Jobs\n (c) Sergery Brin\n",
    "What is Google Inc parent? (a) Alphabet\n (b) Sun Microsoft\n (c) Amazon\n\n",
    "Who is the founder of Globaltech\n (a) Paul Smith\n (b) G.O Asogbon\n (c) Praise Jah\n\n",
    "Who is the president of Germany?\n (a) Angela Merkel (b) Buhari Jones\n (c) Nana Addo\n\n",
    "What is the full meaning of YCMA?\n (a) Young Men Clubbing Activity\n (b) Young Church Movement Action\n (c) Young Men Christain Association\n (d) Young Men Chest Arm\n\n",
    "Which of the following is a name of a continent? (a) South America\n (b) Niger\n (c) Spain\n\n",
    "_____ is the name of a continent and a country? (a) United States\n (b) Australia\n (c) Europe\n\n"
]
# Array that contains instances of Question class and question prompt and the answer
mult_question = [
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "a"),
    Question(question_prompt[3], "b"),
    Question(question_prompt[4], "a"),
    Question(question_prompt[5], "b"),
    Question(question_prompt[6], "a"),
    Question(question_prompt[7], "c"),
    Question(question_prompt[8], "a"),
    Question(question_prompt[9], "b")
]


# run_test takes questions as input. Note it is not the same question array as before
def run_test(questions, time_limit):
    score = 0
    for each_question in questions:
        begin = time()
        engine.say(each_question.prompt)
        engine.runAndWait()
        answer = input(each_question.prompt)
        if answer == each_question.answer:
            score += 1
        end = time()
        diff = end - begin
        if diff >= time_limit:
            print('ending session')
            break
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")
    if score == 0:
        print("\nYour Grade: F")
    elif (score >= 1) and (score <= 4):
        print("\nYour Grade: D")
    elif (score >= 5) and (score <= 6):
        print("\nYour Grade: C")
    elif (score >= 6) and (score < 8):
        print("\nYour Grade: B")
    elif (score > 8) and (score <= 9):
        print("\nYour Grade: B+")
    else:
        print("\nYour Grade: A")


# pass our questions array into run_test function
now = datetime.now()
current_time = now. strftime("%H:%M:%S %p")
print("You started the CBT at ", current_time, "\n\n")
name = str(input("Enter your name\n"))
while not name:
    name = str(input("Please enter your name\n"))
branch = str(input("Where is your branch?\n"))
while not branch:
    branch = str(input("Where is your branch?\n"))
token_number = 7756
num = int(input("Enter Test Token Number\n"))
while not num:
    num = int(input("Enter Test Token Number\n"))
if num == token_number:
    print("\nYou are eligible to take this test\n")
else:
    print("You are not allowed to take this test")
    exit()

start = time()
time_limit = 60
run_test(mult_question, time_limit)
stop = time()
end = datetime.now()
end_time = end.strftime("%H:%M:%S %p")
print("\n\nYou ended the test at ", end_time)
print("You used ", stop - start, " seconds.")
input()
