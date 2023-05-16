# Days of the week Maori
import random

print("This is a test of your knowledge on the Maori words for the days of the week\n"
      " Rā")

# List days in English
English_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List days in Maori
Maori_days = ["Rāhina", "Rātu", "Rāapa", "Rāpare", "Rāmere", "Rāhoroi", "Rātapu"]

question = random.choice(English_days)
attempt = input(f"What is the Maori name for {question}: ")

# Using the index position of the question in one list to find the corresponding index position of the answer
Answer_index = English_days.index(question)
answer = Maori_days[Answer_index]

# Check if user answer correctly
if attempt == answer:
    print("CORRECT")
else:
    print("INCORRECT")
