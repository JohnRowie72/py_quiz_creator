# import necessary libraries for file handling
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import os

# define a function that formats the questions, options, and correct answer
# and into a structured block to be saved in a text file
def format_question_block(question, options, correct_answer):
    block = "[QUESTION]\n"
    block += f"Question: {question}\n"
    block += "[OPTIONS]\n"
    block += f"A: {options['A']}\n"
    block += f"B: {options['B']}\n"
    block += f"C: {options['C']}\n"
    block += f"D: {options['D']}\n"
    block += "[CORRECT_ANSWER]\n"
    block += f"Correct Answer: {correct_answer}\n"
    block += "[END]\n"
    return block

# define a function to append the formatted question block to a text file
def save_question_to_file(filename, data):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(data)

# create the main window (GUI)
class QuizCreatorApp:
    def __init__(self):
        super().__init__()

        self.title("Quiz Creator")
        self.geometry("700x700")
        self.config(bg="#FFEB3B")

        # fonts and colors
        self.font_main = ("Arial", 12)
        self.font_title = ("Arial", 16, "bold")
        self.bg_color = "#FF5722"
        self.bg_color2 = "#FF9800"

        # add tabs using a notebook widget
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # create the tabs for "Create" and "View/Edit"
        self.create_tab = tk.Frame(self.notebook, bg="#FF9800")
        self.view_tab = tk.Frame(self.notebook, bg="#FF9800")
        self.notebook.add(self.create_tab, text="Create Question")
        self.notebook.add(self.view_tab, text="View/Edit Questions")
        
        # create question tab UI
        self.create_question_ui()

        # view/edit questions tab UI
        self.view_edit_ui()

        self.question_count = self.get_question_count()
# run the main function if the script is executed directly
if __name__ == "__main__":
    main()
