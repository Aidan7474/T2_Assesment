# Functions
def yes_no(question_text):
    while True:

        # Ask user if they can speak Maori days of the week
        answer = input(question_text).lower()

        # If yes print "This program is useless to you"
        if answer == "Y" or answer == "y":
            answer = "Yes"
            return answer

        # If no print "This program will help you learn Maori
        if answer == "N" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Answer with Y or N")


# main route
Fluency_Checker = yes_no("Do you know the Maori names for days of the week? ")
if Fluency_Checker == "Yes":
    print("This program will help you learn the Maori days of the week")

if Fluency_Checker == "No":
    print("This program wouldn't help you")
