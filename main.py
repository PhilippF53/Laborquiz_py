from question_model import Question
from quiz_logic import QuizLogic
from quiz_ui import QuizInterface
from quiz_menu import QuizMenu
from random import shuffle
import json

#Open JSON File and load data 
data = open('data.json', "r", encoding="utf-8")
question = json.load(data)

"""
#initialize List and fill it with Question Objects
questions = []
for q in question['questions']:
    print(q)
    choices=[]
    for ans in q['incorrect_answers']:
        choices.append(ans)
    choices.append(q['solution'])
    shuffle(choices)
    questions.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))
#randomize order of questions
shuffle(questions)
"""

def startQuiz():
    menu = QuizMenu()
    questions_mode = []
    while menu.start:
        #seperate questions by mode
        for q in question['questions']:
            match menu.select.get():
                case "Modus 1":
                    if q['mode'] == "m1":
                        choices=[]
                        for ans in q['incorrect_answers']:
                            choices.append(ans)
                        choices.append(q['solution'])
                        shuffle(choices)
                        questions_mode.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))
                    else:
                        continue
                case "Modus 2":
                    if q['mode'] == "m2":
                        choices=[]
                        for ans in q['incorrect_answers']:
                            choices.append(ans)
                        choices.append(q['solution'])
                        shuffle(choices)
                        questions_mode.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))
                    else:
                        continue
                case "Modus 3":
                    if q['mode'] == "m3":
                        choices=[]
                        for ans in q['incorrect_answers']:
                            choices.append(ans)
                        choices.append(q['solution'])
                        shuffle(choices)
                        questions_mode.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))
                    else:
                        continue
        
        #start the quiz with the selected mode
        quiz = QuizLogic(questions_mode)
        quizUI = QuizInterface(quiz)
        if quizUI.end:
            print(menu.select.get())
            menu.start = False
            menu = QuizMenu()
            questions_mode = []
            quizUI.end = False

#finish by closing the file
data.close()

startQuiz()