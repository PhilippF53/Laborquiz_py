class QuizLogic:
    #Initialize QuizLogic Object
    def __init__(self, questions):
        self.questionnr = 0
        self.score = 0
        self.questions = questions
        self.currentQuestion = None
    
    def hasNextQuestion(self):
        #Check if another Question is in the Quiz
        return self.questionnr < len(self.questions)
    
    def nextQuestion(self):
        #get the next Question from the list and return the Question Text
        self.currentQuestion = self.questions[self.questionnr]
        self.questionnr += 1
        questionText = self.currentQuestion.question
        return f"Frage {self.questionnr}: {questionText}"
    
    def checkAnswer(self, userAnswer):
        #return boolean value if the given answer was correct or not
        solution = self.currentQuestion.solution
        if userAnswer.lower() == solution.lower():
            self.score += 1
            return True
        else:
            return False
        
    def getResult(self):
        #Get the number of correct and incorrect answers
        incorrect = self.questionnr - self.score
        return(self.score, incorrect)