# Ask user if they can speak Maori days of the week
fluency_checker = input("Do you know Maori days of the week? : ")

# If yes print "This program is useless to you"
if fluency_checker == "Y":
    print("This program is useless to you")

# If No print "This program will help you learn Maori days of the week"
elif fluency_checker == "N":
    print("This program will help you learn Maori days of the week")

# Otherwise print "Answer with Y or N"
else:
    print("Answer with Y or N")
