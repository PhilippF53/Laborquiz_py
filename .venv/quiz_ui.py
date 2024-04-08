from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_logic import QuizLogic

THEME_COLOR = "blue"

class QuizInterface:

    def __init__(self, quiz_logic: QuizLogic) -> None:
        self.quiz = quiz_logic
        self.window = Tk()
        self.window.title("Quiz Lab")
        self.window.geometry("850x530")
        
        #Creating a canvas for question text
        self.canvas = Canvas(width=800, height=250)
        self.questionText = self.canvas.create_text(200, 50,
                                                     text="Question here", #replaced later
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 15, 'italic'))
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.displayQuestion()

        #Declare a StringVar to store user's answer
        self.userAnswer = StringVar()

        #Display four options(radio buttons)
        self.opts = self.radioButtons()
        self.displayAnswers()

        #To show whether the answer is correct or wrong
        self.feedback = Label(self.window,
                              pady=10,
                              font=("ariel", 15, "bold"))
        self.feedback.place(relx=0.5,
                            y=380,
                            anchor="center")

        #Next, Quit and Info Button
        self.buttons()

        #run the GUI
        self.window.mainloop()
        
    def displayQuestion(self):
        qText = self.quiz.nextQuestion()
        self.canvas.itemconfig(self.questionText, text=qText)
        
    def radioButtons(self):
        #initialize an empty list of answers
        answers = []
        yPos = 220
        
        #initialize 4 Answer fields
        while (len(answers) < 4):
            radioButton = Radiobutton(self.window, 
                                      text="", 
                                      variable=self.userAnswer,
                                      value='', 
                                      font=("ariel", 14))
            answers.append(radioButton)
            radioButton.place(x=100, y=yPos)
            yPos += 40
        
        return answers
    
    def displayAnswers(self):    
        #displaying the four answers
        val = 0
        self.userAnswer.set(None)
        #looping through answer options and filling text of radio buttons
        for option in self.quiz.currentQuestion.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1
            
    def nextButton(self):
        #check if answer is correct
        if self.quiz.checkAnswer(self.userAnswer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer!'
        elif len(self.userAnswer.get()) == None:
            self.feedback["fg"] = "yellow"
            self.feedback["text"] = 'Please select an answer'
            exit()
        else:
            self.feedback["fg"] = "red"
            self.feedback["text"] = ('Ooops!\n'
                                     f'The right answer is: {self.quiz.currentQuestion.solution}')
        #check if there are more questions left
        if self.quiz.hasNextQuestion():
            self.displayQuestion()
            self.displayAnswers()
        #if not display the result
        else:
            self.displayResult()
            self.window.destroy()
    
    def infoButton(self):
        info = self.quiz.currentQuestion.information
        messagebox.showinfo("Information", message=f"{info}")
            
    def buttons(self):
        #show the different buttons
        #first the Next button to move to the next question
        nextButton = Button(self.window, 
                            text="Next",
                            command=self.nextButton,
                            width=10,
                            bg="green",
                            fg="white",
                            font=("ariel", 16, "bold"))
        #place Button on screen
        nextButton.place(relx=0.50, 
                         y=460,
                         anchor="center")
        #initialize the Quit button to exit the App
        quitButton = Button(self.window,
                            text="Quit",
                            command=self.window.destroy,
                            width=5,
                            bg="red",
                            fg="white",
                            font=("ariel", 16, "bold"))
        quitButton.place(relx=0.1,
                         y=460,
                         anchor="center")
        #initialize Information button
        infoButton = Button(self.window,
                            text="Info",
                            command=self.infoButton,
                            width=5,
                            bg="blue",
                            fg="white",
                            font=("ariel", 16, "bold"))
        infoButton.place(relx=0.9,
                         y=460,
                         anchor="center")
        
    def displayResult(self):
        #display the result using a messagebox
        correct, incorrect = self.quiz.getResult()
        correct = f"Correct: {correct}"
        incorrect = f"Incorrect: {incorrect}"
        messagebox.showinfo("Result", f"{correct}\n{incorrect}")