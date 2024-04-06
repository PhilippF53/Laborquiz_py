import json;

#Define Question Object
class Question: 
    def __init__(self, mode:str, question: str, solution: str, choices: list, information:str):
        self.mode = mode
        self.question_text = question
        self.solution = solution
        self.choices = choices
        self.information = information