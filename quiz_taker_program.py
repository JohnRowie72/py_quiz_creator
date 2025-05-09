# import necessary libraries for GUI and file handling
import tkinter as tk
from tkinter import messagebox
import random

# define a function to load quiz questions from a text file
def load_questions_data(filename="quiz_storage.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read().strip()

    blocks = content.split("Question: ")[1:]
    questions = []

    for block in blocks:
        # parse each line in the block to extract questions and options
        lines = block.strip().splitlines()
        question_text = lines[0].strip()
        options = {
            "option_a": lines[2].strip("option_a: ")[1].strip(),
            "option_b": lines[3].strip("option_b: ")[1].strip(),
            "option_c": lines[4].strip("option_c: ")[1].strip(),
            "option_d": lines[5].strip("option_d: ")[1].strip(),
        }
        correct_answer = lines[6].strip("correct_answer: ")[1].strip()
        # store the parsed question data into the list
        questions.append({
            "question": question_text,
            "options": options,
            "correct_answer": correct_answer
        })

    #shuffle the list of questions randomly
    random.shuffle(questions)
    return questions
    
# define a class for the quiz application
class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #set up the main window
        self.title("🔥 Quiz Taker 🔥")
        self.geometry("800x600")
        self.configure(bg="#222831")

        # load quiz questions and intialize counters
        self.questions = load_questions_data()
        self.current_question_index = 0
        self.user_answers = []

        self.create_widgets()
        self.load_question()

    # create the UI components
    def create_widgets(self):
        self.title_label = tk.Label(self, text="QUIZ TIME", font=("Helvetica", 24, "bold"), fg="#FFD369", bg="#222831")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(self, text="", font=("Helvetica", 16), fg="white", bg="#222831", wraplength=700, justify="center")
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(self, bg="#222831")
        self.options_frame.pack(pady=10)

        self.selected_answer = tk.StringVar(value="")

        self.option_buttons = {}
        for key in ['option_a', 'option_b', 'option_c', 'option_d']:

            # create radio buttons for each option
            btn = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_answer,
                value=key,
                font=("Helvetica", 13),
                bg="#393E46",
                fg="white",
                wraplength=650,
                justify="left",
                indicatoron=0,
                width=60,
                height=3,
                pady=10,
                selectcolor="#FFD369",
                activebackground="#00ADB5"
            )
            btn.pack(pady=1, anchor="w")
            self.option_buttons[key] = btn

        #create a submit button
        self.submit_button = tk.Button(self, text="Submit Answer", command=self.submit_answer, font=("Helvetica", 14), bg="#00ADB5", fg="white")
        self.submit_button.pack(pady=20)

    # load the quiz question into the UI
    def load_question(self):
        if self.current_index < len(self.questions):
            current_question = self.questions[self.current_index]
            self.question_label.config(text=current_question["question"])
            self.selected_answer.set("")

            for key, btn in self.option_buttons.items():
                btn.config(text=current_question["options"][key], state=tk.NORMAL)

        else:
            self.show_results()
                    
    # handle the user's answer
    # display quiz results
    # function to restart the quiz
# run the program