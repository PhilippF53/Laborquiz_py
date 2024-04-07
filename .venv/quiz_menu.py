from tkinter import Tk, Label, Radiobutton, Button, messagebox

class QuizMenu:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Laborquiz")
        self.window.geometry("850x530")
        self.start = False
        
        self.placeTitle()
        self.button()
        self.window.mainloop()
    
    #display title of the App    
    def placeTitle(self):
        title = Label(self.window, text="Laborquiz", width=30, bg="lightblue", fg="black", font=("ariel", 20, "bold"))
        title.place(relx=0.5, y=20, anchor="center")
    
    
    def startQuiz(self):
        self.start = True
        self.window.destroy()
        
    def button(self):
        #initialize button to start the quiz
        startButton = Button(self.window, text="Start", command=self.startQuiz, width=5, bg="gray", fg="black", font=("ariel", 16, "bold"))
        startButton.place(relx=0.5, y=200, anchor="center")
        #initialize the button to end the quiz
        quitButton = Button(self.window, text="Quit", command=self.window.destroy, width=5, bg="red", fg="white", font=("ariel", 16, "bold"))
        quitButton.place(relx=0.5, y=300, anchor="center")
        
    