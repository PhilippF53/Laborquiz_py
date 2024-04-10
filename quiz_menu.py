from tkinter import *

class QuizMenu:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quiz Lab")
        self.window.geometry("850x530")
        self.start = False
        self.select = StringVar()

        self.window.update_idletasks()
        self.window.update()
        self.window.configure(bg="lightblue")
        self.placeTitle()
        self.button()
        self.modeSelect()
        self.window.mainloop()
    
    #display title of the App    
    def placeTitle(self):
        title = Label(self.window,
                      text="Quiz Lab",
                      width=self.window.winfo_reqwidth(),
                      bg="lightblue",
                      fg="black",
                      font=("ariel", 20, "bold"))
        title.place(relx=0.5,
                    y=20,
                    anchor="center")
    
    
    def startQuiz(self):
        self.start = True
        self.window.destroy()
        
    def button(self):
        #initialize button to start the quiz
        startButton = Button(self.window,
                             text="Start",
                             command=self.startQuiz,
                             width=8,
                             bg="green",
                             fg="black",
                             font=("ariel", 16, "bold"))
        startButton.place(relx=0.5,
                          y=300,
                          anchor="center")
    
    def modeSelect(self):
        options = [
                "Modus 1",
                "Modus 2",
                "Modus 3"
            ]
        self.select.set(options[0])
        
        info = Label(self.window,
                     text="Spielmodus auswählen:",
                     width=0,
                     bg="lightblue",
                     fg="black",
                     font=("ariel", 16))
        info.place(relx=0.5, y=200, anchor="center")
        
        self.drop = OptionMenu(self.window, self.select, *options)
        self.drop.place(relx=0.5, y=250, anchor="center")
        