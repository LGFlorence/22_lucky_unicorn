# Function
def num_check(question, low, high):
    # Main routine

    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask question
            response = int(input(question))

            # if amount is too low/too high give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# main routine
how_much = num_check("How much would you like to play with?",0, 10)

print("You will be spending ${}".format(how_much))
