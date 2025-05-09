# import necessary libraries for GUI and file handling
import tkinter as tk
from tkinter import messagebox
import random

# define a function to load quiz questions from a text file
def load_quesitons_data(filename="quiz_storage.txt"):
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
# define a function to create the GUI components
    # create the UI components
    # load the quiz question into the UI
    # handle the user's answer
    # display quiz results
    # function to restart the quiz
# run the program