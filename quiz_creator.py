# import necessary libraries for file handling
import os

# define a function that formats the questions, options, and correct answer
# and into a structured block to be saved in a text file
def format_question_block(question, options, correct_answer):
    block + "[QUESTION]\n"
    block += f"Question: {question}\n"
    block += "[OPTIONS]\n"
    block += f"A: {options[A]}\n"
    block += f"B: {options[B]}\n"
    block += f"C: {options[C]}\n"
    block += f"D: {options[D]}\n"
    block += "[CORRECT_ANSWER]\n"
    block += f"Correct Answer: {correct_answer}\n"
    block += "[END]\n"
    return block

# define a function to append the formatted question block to a text file
def save_question_to_file(filename, data):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(data)
        
# define a function to validate the correct answer input
# keeps asking until a valid input is provided
# define the main logic to create a quiz
# loop to repeatedly ask for quiz questions and store them in a file
# run the main function if the script is executed directly
