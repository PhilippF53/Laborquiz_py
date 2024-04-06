import json;

#Define Question Object
class Question: 
    def __init__(self, mode:str, question: str, solution: str, incorrect_answers: list, information:str):
        self.mode = mode
        self.question_text = question
        self.solution = solution
        self.incorrect_answers = incorrect_answers
        self.information = information

#Open JSON File and load data 
data = open('.venv/data.json', "r", encoding="utf-8")
question = json.load(data)

#initialize List and fill it with Question Objects
questions = []
for q in question['question']:
    print(q)
    questions.append(Question(q['mode'], q['question'], q['solution'], q['incorrect_answers'], q['information']))

#finish by closing the file
data.close()