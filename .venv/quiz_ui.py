from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_logic import QuizLogic

THEME_COLOR = '#375262'

class QuizInterface:

    def __init__(self, quiz_logic: QuizLogic) -> None:
        self.quiz = quiz_logic
        self.window = Tk()
        self.window.title("Laborquiz")
        self.window.geometry("850x530")
        
        #Creating a canvas for question text, and dsiplay question
        self.canvas = Canvas(width=800, height=250)
        self.questionText = self.canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=('Ariel', 15, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.displayQuestion()

        #Declare a StringVar to store user's answer
        self.userAnswer = StringVar()

        #Display four options(radio buttons)
        self.opts = self.radioButtons()
        self.displayAnswers()

        #To show whether the answer is correct or wrong
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        #Next and Quit Button
        self.buttons()

        #Mainloop
        self.window.mainloop()
        
    def displayQuestion(self):
        qText = self.quiz.nextQuestion
        self.canvas.itemconfig(self.questionText, text=qText)
        
    def radioButtons(self):
        #initialize an empty list of answers
        answers = []
        yPos = 220
        
        #initialize 4 Answer fields
        while (len(answers) < 4):
            radioButton = Radiobutton(self.window, text="", variable=self.userAnswer,
                                    value='', font=("ariel", 14))
            answers.append(radioButton)
            radioButton.place(x=200, y=yPos)
            yPos += 40
        
        return answers
    
    def displayAnswers(self):    
        #displaying the four answers
        val = 0
        self.userAnswer.set(None)
        #looping through answer options and filling text of radio buttons
        for option in (self.quiz.currentQuestion.solution & self.quiz.currentQuestion.incorrect_answers):
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1
            
    def nextButton(self):
        #check if answer is correct
        if self.quiz.checkAnswer(self.userAnswer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback["fg"] = "red"
            self.feedback["text"] = ('\u274E Ooops!\n'
                                     f'The right answer is: {self.quiz.currentQuestion.solution}')
        #check if there are more questions left
        if self.quiz.hasNextQuestion():
            self.displayQuestion()
            self.displayAnswers()
        #if not display the result
        else:
            self.displayResult()
            
    def buttons(self):
        #show the different buttons
        #first the Next button to move to the next question
            
        
    def displayResult(self):
        #display the result using a messagebox
        correct, incorrect = self.quiz.getResult()
        correct = f"Correct: {correct}"
        incorrect = f"Incorrect: {incorrect}"
        
        messagebox.showinfo("Result", f"{correct}\n{incorrect}")
            
        
        