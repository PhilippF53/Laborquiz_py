from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox, PhotoImage, Toplevel
from quiz_logic import QuizLogic

THEME_COLOR = "black"


class QuizInterface:

    def __init__(self, quiz_logic: QuizLogic) -> None:
        self.quiz = quiz_logic
        self.window = Tk()
        self.window.title("Quiz Lab")
        self.window.geometry("1700x1060")
        self.window.configure(bg="lightblue")
        self.end = False

        # Creating a canvas for question text
        self.canvas = Canvas(width=1500, height=500, highlightthickness=1, highlightbackground="black")
        self.questionText = self.canvas.create_text(50, 200,
                                                    text="Frage hier",  # wird später ersetzt
                                                    anchor="w",
                                                    width=1500,
                                                    fill=THEME_COLOR,
                                                    font=('Arial', 18, 'italic'))
        self.canvas.grid(row=0, column=0, columnspan=1, pady=50, padx=100)
        self.displayQuestion()

        # Declare a StringVar to store user's answer
        self.userAnswer = StringVar()

        # Display four options (radio buttons)
        self.opts = self.radioButtons()
        self.displayAnswers()

        # To show whether the answer is correct or wrong
        self.feedback = Label(self.window,
                              bg="lightblue",
                              pady=10,
                              font=("Arial", 15, "bold"))
        self.feedback.place(relx=0.5,
                            y=780,
                            anchor="center")

        # Next, Quit, Info, and Cheat Sheet Button
        self.buttons()

        # Run the GUI
        self.window.mainloop()

    def displayQuestion(self):
        qText = self.quiz.nextQuestion()
        self.canvas.itemconfig(self.questionText, text=qText)

    def radioButtons(self):
        # Initialize an empty list of answers
        answers = []
        yPos = 560

        # Initialize 4 Answer fields
        while len(answers) < 4:
            radioButton = Radiobutton(self.window,
                                      bg="lightblue",
                                      text="",
                                      variable=self.userAnswer,
                                      value='',
                                      font=("Arial", 14))
            answers.append(radioButton)
            radioButton.place(x=220, y=yPos + 20, anchor="w")
            yPos += 60

        return answers

    def displayAnswers(self):
        # Displaying the four answers
        val = 0
        self.userAnswer.set(None)
        # Loop through answer options and set text of radio buttons
        for option in self.quiz.currentQuestion.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def nextButton(self) -> object:
        # Check if answer is correct
        if self.quiz.checkAnswer(self.userAnswer.get()):
            self.feedback["fg"] = "white"
            self.feedback["bg"] = "#6aa84a"
            self.feedback["text"] = 'Richtig!'
        else:
            self.feedback["fg"] = "white"
            self.feedback["bg"] = "#af504c"
            self.feedback["text"] = (f'Falsch!\n'
                                     f'Die richtige Antwort war: {self.quiz.currentQuestion.solution}')
        # Check if there are more questions left
        if self.quiz.next_question():
            self.displayQuestion()
            self.displayAnswers()
        # If not, display the result
        else:
            self.displayResult()
            self.end = True
            self.window.destroy()

    def quitButton(self):
        self.end = True
        self.window.destroy()

    def infoButton(self):
        info = self.quiz.currentQuestion.information
        messagebox.showinfo("Information", message=f"{info}")

    def cheatSheet(self):
        novi = Toplevel()
        novi.title("Spickzettel")
        canvas = Canvas(novi, width=1200, height=1000, bg="lightblue")
        canvas.pack(expand="yes", fill="both")
        # Laden Sie das Bild für den Spickzettel
        spickzettel_image = PhotoImage(file="spickzettel.png")
        canvas.create_image(50, 10, image=spickzettel_image, anchor="nw")
        canvas.image = spickzettel_image

    def buttons(self):
        button_width = 12
        button_height = 2
        button_font = ("Arial", 14, "bold")

        # Next button
        nextButton = Button(self.window,
                            text="Weiter",
                            command=self.nextButton,
                            width=button_width + 5,
                            height=button_height,
                            bg="#4CAF50",
                            fg="white",
                            font=button_font)
        nextButton.place(relx=0.58, rely=0.9, anchor="s")

        # Quit button
        quitButton = Button(self.window,
                            text="Zurück zum Menü",
                            command=self.quitButton,
                            width=button_width + 5,
                            height=button_height,
                            bg="#e06666",
                            fg="white",
                            font=button_font)
        quitButton.place(relx=0.45, rely=0.9, anchor="s")

        # Info button
        infoButton = Button(self.window,
                            text="Hinweis",
                            command=self.infoButton,
                            width=button_width,
                            height=button_height,
                            bg="#0b5394",
                            fg="white",
                            font=button_font)
        infoButton.place(relx=0.94, rely=0.30, anchor="s")

        cheatSheet = Button(self.window,
                            text="Spickzettel",
                            command=self.cheatSheet,
                            width=button_width,
                            height=button_height,
                            bg="#0b5394",
                            fg="white",
                            font=button_font)
        cheatSheet.place(relx=0.94, rely=0.35, anchor="s")

        # Styling radio buttons
        for radioButton in self.opts:
            radioButton.config(bg="lightblue", font=("Arial", 14))

    def displayResult(self):
        # Display the result using a messagebox
        correct, incorrect = self.quiz.getResult()
        correct = f"Richtig: {correct}"
        incorrect = f"Falsch: {incorrect}"
        messagebox.showinfo("Ergebnis", f"{correct}\n{incorrect}")

