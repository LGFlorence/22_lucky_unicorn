# function
def yes_no(question):
    valid = False

    while not valid:
        # Ask user is they have played before
        response = input(question).lower().strip()

        # if user types yes output 'Program continues'
        if "yes" in response or response == "y":
            response = "yes"
            return response

    # if user types no output 'Display instructions'
        elif "no" in response or response == "n":
            response = "no"
            return response

    else:
        print("Please enter yes/no")


# Main routine
show_instructions = yes_no("Have you played this game before.").lower()
print("You choose {}".format(show_instructions))





