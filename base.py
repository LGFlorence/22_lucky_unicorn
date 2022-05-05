import random


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


def instructions():
    print("--- How to play---")
    print()
    print("You will have a maximum of 10 dollars to play this game, each round costs $1\n"
          "Every round a token will be generated, either a unicorn, zebra, horse or donkey.\n"
          "If the token is a unicorn,  you win $5, if it is a zebra or horse, you win 50c and if it is a donkey then you don’t win anything.\n"
          "The game will continue until you have either lost all your money or you decide to quit while your ahead.\n"
          "\n"
          "The key objective is to try and make as much money as you can without taking too much of a risk that you lose it all.\n"
          "\n"
          "Good luck\n")
    print()
    return ""


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


def statement_generator(statement, decoration) -> object:
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main routine

outcome = "Welcome to the Lucky Unicorn Game"
prize_decoration = "|"
statement_generator(outcome, prize_decoration)

print()
played_before = yes_no("Have you played the game before?")

if played_before == "no":
    print()
    print(instructions())

print("Program continues")
print()

# ask user how much they want to play with
how_much = num_check("How much would you like to play with?", 0, 10)

balance = how_much

rounds_played = 0

print()

play_again = input("Press <Enter> to play").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number
    print()
    print()
    print("*** Round #{} ***".format(rounds_played))
    print()

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if random # is between 1 and 5,
    # user gets unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = ">"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    # the token is either a horse or zebra
    # in both cases, subtract $.50 from balance
    else:
        # if the number is even set chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # otherwise set to zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
            balance -= 0.5

    outcome = "You got a {}    Your balance is " \
              "${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print()
        print("Sorry you have run out of money")
    else:
        print()
        play_again = input("Press Enter to play again "
                           "or 'xxx' to quit")

print()
print("Final balance $", balance)
