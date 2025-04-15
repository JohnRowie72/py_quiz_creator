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

    def create_question_ui(self):
        # labels and inputs for creating questions
        tk.Label(self.create_tab, text="Enter Quiz Question:", font=self.font_title, bg="#FFEB3B").pack(pady=10)
        self.question_entry = tk.Entry(self.create_tab, font=self.font_main, width=50)
        self.question_entry.pack(pady=5)

        tk.Label(self.create_tab, text="Enter Options:", font=self.font_title, bg="#FFEB3B").pack(pady=10)
        self.options = {}
        for choice in ['A', 'B', 'C', 'D']:
            label = f"Option {choice}:"
            self.options[choice] = tk.Entry(self.create_tab, font=self.font_main, width=50)
            tk.Label(self.create_tab, text=label, font=self.font_main, bg="#FFEB3B").pack(pady=5)
            self.options[choice].pack(pady=5)
        
        tk.label(self.create_tab, text="Select Correct Answer:", font=self.font_title, bg="#FFEB3B").pack(pady=10)
        self.correct_answer = ttk.Combobox(self.create_tab, values=['A', 'B', 'C', 'D'], font=self.font_main, state="readonly")
        self.correct_answer.pack(pady=5)

        # save question button
        self.save_button = tk.Button(self.create_tab, text="Save Question", font=self.font_main, bg=self.bg_color, command=self.save_question)
        self.save_button.pack(pady=10)
    
    def save_questions(self):
        question = self.question_entry.get().strip()
        if not question:
            messagebox.showwarning("Error", "Please enter a question.")
            return

        options = {key: entry.get().strip() for key, entry in self.options.items()}
        if not all(options.values()):
            messagebox.showwarning("Error", "Please enter all options.")
            return

        correct_answer = self.correct_answer.get()
        if not correct_answer:
            messagebox.showwarning("Error", "Please select a correct answer.")
            return

        # format the question block and save it to a file
        filename = "quiz_storage.txt"
        self.question_count += 1
        block = format_question_block(question, options, correct_answer, self.question_count)
        save_question_to_file(filename, block)

        messagebox.showinfo("Success", "Question saved successfully!")
        self.clear_inputs()
        self.load_questions()

    def clear_inputs(self):
        self.question_entry.delete(0, tk.END)
        for entry in self.options.values():
            entry.delete(0, tk.END)
        self.correct_answer.set('')
    
    def get_question_count(self):
        if not os.path.exists("quiz_storage.txt"):
            return 0
        with open("quiz_storage.txt", "r", encoding="utf-8") as file:
            return sum(1 for line in file if line.startswith("[QUESTION]"))
    
    def view_edit_ui(self):
        # text area to display questions from the file
        self.question_display = ScrolledText(self.view_tab, width=70, height=15, font=self.font_main)
        self.question_display.pack(pady=10)
        self.load_questions()

        # edit and delete buttons
        self.edit_button = tk.Button(self.view_tab, text="Edit Selected Question", font=self.font_main, bg=self.bg_color, command=self.edit_question)
        self.edit_button.pack(pady=10)

        self.delete_button = tk.Button(self.view_tab, text="Delete Selected Question", font=self.font_main, bg=self.bg_color2, command=self.delete_question)
        self.delete_button.pack(pady=10)
        
    def load_questions(self):
        # load the questions from the file and display them
        try:
            with open("quiz_storage.txt", "r", encoding="utf-8") as file:
                content = file.read()
                self.question_text.delete(1.0, tk.END)
                self.question_text.insert(tk.END, content)
        except FileNotFoundError:
            self.question_display.insert(tk.END, "No questions found.")
    
# run the main function if the script is executed directly
if __name__ == "__main__":
    main()
