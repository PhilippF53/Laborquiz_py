import tkinter as tk
from tkinter import ttk
from question_model import Question
from quiz_logic import QuizLogic
from quiz_ui import QuizInterface
from random import shuffle
import json

class QuizMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Lab")
        self.window.geometry("850x530")
        self.window.configure(bg="lightblue")
        self.start = False
        self.selected_option = tk.StringVar(self.window)
        self.selected_option.set("Modus 1")

        self.place_title()
        self.modeSelect()
        self.create_button()
        self.window.mainloop()

    def place_title(self):
        title_label = tk.Label(self.window, text="Quiz Lab", font=("Arial", 40, "bold"), bg="lightblue", fg="#333333")
        title_label.pack(pady=50)

    def startQuiz(self):
        self.start = True
        self.window.destroy()

    def create_button(self):
        start_button = tk.Button(self.window, text="Start", command=self.startQuiz, width=5, bg="#4CAF50", fg="white", font=("Arial", 25, "bold"), bd=0, padx=60, pady=5)
        start_button.pack(pady=20)

    def modeSelect(self):
        mode_frame = tk.Frame(self.window, bg="lightblue")
        mode_frame.pack(pady=20)

        info_label = tk.Label(mode_frame, text="Spielmodus auswählen:", font=("Arial", 18), bg="lightblue", fg="#333333")
        info_label.pack()

        dropdown = ttk.Combobox(mode_frame, textvariable=self.selected_option, values=["Modus 1", "Modus 2", "Modus 3"], state="readonly", width=20, font=("Arial", 14))
        dropdown.pack(pady=10)
        dropdown.config(background="white", foreground="black", font=("Arial", 15))


