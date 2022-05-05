import random

# main routine

tokens = [" unicorn", "horse", "zebra", "donkey"]

# Testing loop to generate 20 tokens
for item in range(0, 20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')

