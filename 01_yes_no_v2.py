show_instructions = ""

while show_instructions.lower != "":
    # Ask user is they have played before
    show_instructions = input("Have you played this game before.").lower()

    # if user types yes output 'Program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # if user types no output 'Display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("Display instructions")

    else:
        print("Please enter yes/no")


