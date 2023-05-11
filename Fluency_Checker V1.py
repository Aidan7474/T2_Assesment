# Ask user if they can speak Maori fluently
fluency_checker = input("Can you speak Maori fluently? : ")

# If yes print "This program is to easy for you"
if fluency_checker == "Y":
    print("This test is to easy for you")

# If No print "This test will help you learn Maori"
elif fluency_checker == "N":
    print("This test will help you learn Maori")

# Otherwise print "Answer with Y or N"
else:
    print("Answer with Y or N")
