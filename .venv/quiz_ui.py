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
        self.opts = self.radio_buttons()
        self.display_options()

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
        
    def 
        
        