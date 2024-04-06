from question_model import Question
from quiz_logic import QuizLogic
from quiz_ui import QuizInterface
from random import shuffle
import json

#Open JSON File and load data 
data = open('.venv/data.json', "r", encoding="utf-8")
question = json.load(data)

#initialize List and fill it with Question Objects
questions = []
#for q in question['question']:
#    print(q)
#    questions.append(Question(q['mode'], q['question'], q['solution'], q['incorrect_answers'], q['information']))

questionBank = []
for quest in question['question']:
    #build the question
    choices = []
    mode = quest['mode']
    questionText = quest['question']
    solution = quest['solution']
    incorrect_answers = quest['incorrect_answers']
    information = quest['information']
    for ans in incorrect_answers:
        choices.append(ans)
    choices.append(solution)
    #randomize the order of the answers
    shuffle(choices)
    newQuestion = Question(mode, question, solution, choices, information)
    questionBank.append(newQuestion)
    
#finish by closing the file
data.close()

quiz = QuizLogic(questionBank)
quizUI = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.questionnr}")