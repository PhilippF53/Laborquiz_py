from question_model import Question
from quiz_logic import QuizLogic
from quiz_ui import QuizInterface
from quiz_menu import QuizMenu
from random import shuffle
import json

#Open JSON File and load data 
data = open('.venv/data.json', "r", encoding="utf-8")
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
        selected_mode = menu.selected_option.get()
        for q in question['questions']:
            if selected_mode == "Modus 1" and q['mode'] == "m1":
                choices = q['incorrect_answers'] + [q['solution']]
                shuffle(choices)
                questions_mode.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))
            elif selected_mode == "Modus 2" and q['mode'] == "m2":
                choices = q['incorrect_answers'] + [q['solution']]
                shuffle(choices)
                questions_mode.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))
            elif selected_mode == "Modus 3" and q['mode'] == "m3":
                choices = q['incorrect_answers'] + [q['solution']]
                shuffle(choices)
                questions_mode.append(Question(q['mode'], q['question'], q['solution'], choices, q['information']))

        quiz = QuizLogic(questions_mode)
        quizUI = QuizInterface(quiz)
        if quizUI.end:
            print(selected_mode)
            menu.start = False
            menu = QuizMenu()
            questions_mode = []

    data.close()

startQuiz()
