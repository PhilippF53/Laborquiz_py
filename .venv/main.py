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

#finish by closing the file
data.close()
    
"""
questionBank = []
for quest in question['question']:
    #build the question
    choices = []
    mode = quest['mode']
    questionText = quest['question']
    solution = quest['solution']
    incorrect_answers = quest['incorrect_answers']
    information = quest['information']
    #build the choices
    for ans in incorrect_answers:
        choices.append(ans)
    choices.append(solution)
    
    #randomize the order of the answers
    shuffle(choices)
    newQuestion = Question(mode, question, solution, choices, information)
    questionBank.append(newQuestion)
"""

def startQuiz():
    menu = QuizMenu() 
    if menu.start:
        quiz = QuizLogic(questions)
        quizUI = QuizInterface(quiz)

startQuiz()