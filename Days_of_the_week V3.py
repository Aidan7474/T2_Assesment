# Days of the week Maori
import random
# give variables values
correct_answers = 0
attempted_questions = 0
print("This is a test of your knowledge on the Maori words for the days of the week")

# List days in English
English_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List days in Maori
Maori_days = ["rahina", "ratu", "raapa", "rapare", "ramere", "rahoroi", "ratapu"]

# While loop
while attempted_questions < 10:

    # User input on question
    question = random.choice(English_days)
    attempt = input(f"What is the Maori name for {question}: ")
    attempted_questions += 1

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
    print(f"Your score is {correct_answers} out of {attempted_questions}")
