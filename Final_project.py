# Import random
import random


# Functions
def yes_no(question_text):
    while True:

        # Ask user if they can speak Maori days of the week
        yes_no_answer = input(question_text).lower()

        # If yes print "This program is useless to you"
        if yes_no_answer == "N" or yes_no_answer == "n":
            yes_no_answer = "No"
            return yes_no_answer

        # If no print "This program will help you learn Maori
        if yes_no_answer == "Y" or yes_no_answer == "y":
            yes_no_answer = "Yes"
            return yes_no_answer

        # Otherwise - ask user to answer with Y or N
        else:
            print("Answer with Y or N\n"
                  " ")


# Input on user fluency
Fluency_Checker = yes_no("Do you know the Maori names for days of the week?\n"
                         " ")
if Fluency_Checker == "No":
    print("This program will help you learn the Maori days of the week\n"
          " ")

if Fluency_Checker == "Yes":
    print("This program wouldn't help you\n"
          " ")

# give variables values
correct_answers = 0
possible_questions = 0
print("This is a test of your knowledge on the Maori words for the days of the week\n"
      " ")

# List days in English
English_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List days in Maori
Maori_days = ["rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi", "ratapu"]

# How many questions there should be
no_of_questions = int(input("How many questions do you want? \n"
                            ""))
while possible_questions < no_of_questions:

    # User input on question
    question = random.choice(English_days)
    attempt = input(f"What is the Maori name for {question}:\n"
                    f" ")
    possible_questions += 1

    # Use English_days as question variable and Maori_days as answer
    Answer_index = English_days.index(question)
    answer = Maori_days[Answer_index]

    # Check if user answer correctly
    if attempt == answer:
        correct_answers += 1
        print("CORRECT")
    else:
        print(f"INCORRECT \n"
              f"THE CORRECT ANSWER IS {answer}")

    # score user
    print(f"Your score is {correct_answers} out of {possible_questions}")
