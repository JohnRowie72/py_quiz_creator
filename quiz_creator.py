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
def get_valid_answer(prompt_message, valid_choices):
    while True:

        # ask the user for input and convert the input to uppercase and remove leading/trailing spaces
        answer = input(prompt_message).strip().upper()
        if answer in valid_choices:
            return answer
        else:
            print(f"Invalid input. Please choose from {', '.join(valid_choices)}.")

# define the main logic to create a quiz
# loop to repeatedly ask for quiz questions and store them in a file
def main():
    filename = "quiz_bank.txt"
    print("📚 Welcome to the Quiz Creator!")
    print("Create as many questions as you want. Type 'exit' to stop.\n")

    while True:
        # ask the user for a quiz question
        question = input("❓ Enter your quiz question (or type 'exit' to finish): ").strip()
        if question.lower() == 'exit':
            print("👋 Exiting Quiz Creator. All data saved.")
            break

        # ask the user for options A, B, C, and D
        # ask the user for the correct answer
        # format the question block and save it to the file
# run the main function if the script is executed directly
