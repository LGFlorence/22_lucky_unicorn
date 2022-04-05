# ask user if played before
show_instructions = input("Have you work played this game before").lower()

# if user types yes output 'program continues'
if show_instructions == "yes":
    print("Program continues")

elif show_instructions == "y":
    print("Program continues")

# if user types no output 'display instructions'
elif show_instructions == "no":
    print("Display instructions")

elif show_instructions == "n":
    print("Program continues")


else:
    print("Please answer yes/no")
