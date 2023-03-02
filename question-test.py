import threading
from pynput.keyboard import Key, Controller

question_prompt = [
    "Where is Lamborghini made? \n(a) Germany\n (b) Italy\n (c) Nigeria\n\n",
    "Who is the first man to travel to space? \n(a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n",
    "Who is the first man to land on the moon? \n(a) Neil Armstrong\n (b) Yuri Gagarin\n (c) Micheal Jackson\n\n",
    "Who is the founder of Apple Inc.? \n(a) Mark Zuckerberg\n (b) Steve Jobs\n (c) Sergery Brin\n",
    "What is Google Inc parent? \n(a) Alphabet\n (b) Sun Microsoft\n (c) Amazon\n\n",
    "Who is the founder of Globaltech \n(a) Paul Smith\n (b) G.O Asogbon\n (c) Praise Jah\n\n",
    "Who is the president of Germany? \n(a) Angela Merkel (b) Buhari Jones\n (c) Nana Addo\n\n",
    "What is the full meaning of YCMA? \n(a) Young Men Clubbing Activity\n (b) Young Church Movement Action\n (c) Young Men Christian Association\n (d) Young Men Chest Arm\n\n",
    "Which of the following is a name of a continent? \n(a) South America\n (b) Niger\n (c) Spain\n\n",
    "_____ is the name of a continent and a country? \n(a) United States\n (b) Australia\n (c) Europe\n\n",
]

quiz_timer = 5 * 60 # 5 mins converted to seconds

KEYBOARD = Controller()

class Question:
    def __init__(self, question_prompt, answer, quiz: "Quiz") -> None:
        self.question_prompt = question_prompt
        self.answer = answer
        self.quiz = quiz
        self.score = 0

    def run(self):
        answer = input(self.question_prompt)
        if answer == self.answer:
            self.score = 1
            self.quiz.score += 1
        self.quiz.counter += 1
            

class Quiz:
    def __init__(self) -> None:
        self.multi_questions = []
        self.timer = threading.Timer(5, self.end_quiz_due_to_timer)
        self.quiz_run = True
        self.score = 0

    def add_questions(self, questions):
        for question in questions:
            self.multi_questions.append(Question(question_prompt, ))

    def end_quiz_due_to_timer(self):
        self.quiz_run = False
        KEYBOARD.press(Key.enter)
        KEYBOARD.release(Key.enter)

    def next_question(self):
        self.counter += 1

    def run(self):
        self.counter = 0 
        self.timer.start()
        while self.quiz_run:
            while self.counter < len(self.multi_questions):
                self.multi_questions[self.counter].run()
                break
            
            if self.counter >= len(self.multi_questions):
                self.quiz_run = False
                self.timer.cancel()

        print(f"Your score is {self.score}")



quiz = Quiz()

multi_question = [
    Question(question_prompt[0], "b", quiz),
    Question(question_prompt[1], "b", quiz),
    Question(question_prompt[2], "a", quiz),
    Question(question_prompt[3], "b", quiz),
    Question(question_prompt[4], "a", quiz),
    Question(question_prompt[5], "b", quiz),
    Question(question_prompt[6], "a", quiz),
    Question(question_prompt[7], "c", quiz),
    Question(question_prompt[8], "a", quiz),                           
    Question(question_prompt[9], "b", quiz),
]

for q in multi_question:
    quiz.multi_questions.append(q)


quiz.run()