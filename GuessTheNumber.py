
# Guess the Number Game


# Choose a number and pc would guess it
# if it is lower enter l 
# else if it is greater enter g
# if it is correct enter c

import random
min = 1
max = 99
guess = random.randint(min,max)
previous_guess = 0
print(guess)
answer = input()

while answer != 'c':
    if answer == 'g':
        min = guess
    if answer == 'l':
        max = guess
    guess = random.randint(min,max)
    while(guess == previous_guess):
        guess = random.randint(min,max)
    print(guess)
    answer = input()
    previous_guess = guess

print('\n :)')
