from question_model import Question
from quiz_logic import QuizLogic
from quiz_ui import QuizInterface
from quiz_menu import QuizMenu
from random import shuffle
import json

#Open JSON File and load data 
data = open('.venv/data.json', "r", encoding="utf-8")
question = json.load(data)

#initialize List and fill it with Question Objects
questions = []
for q in question['question']:
#    print(q)
    choices=[]
    for ans in q['incorrect_answers']:
        choices.append(ans)
    choices.append(q['solution'])
    shuffle(choices)
    questions.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))

#randomize order of questions
shuffle(questions)
#finish by closing the file
data.close()

def startQuiz():
    menu = QuizMenu() 
    while menu.start:
        quiz = QuizLogic(questions)
        quizUI = QuizInterface(quiz)
        if quizUI.end:
            menu.start = False
            menu = QuizMenu()
            quizUI.end = False

startQuiz()